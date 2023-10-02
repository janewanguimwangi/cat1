import pandas as pd
import glob, os

file_path = 'data/en-US.jsonl'
directory_path = 'data'
output_folder = 'output/q1'

en_df = pd.read_json(path_or_buf=file_path, lines=True)
# Select only the desired columns
selected_columns = ['id', 'utt', 'annot_utt']
en_df = en_df[selected_columns]

# Get a list of JSONL file paths in the directory
jsonl_files = glob.glob(f'{directory_path}/*.jsonl')

for file_path in jsonl_files:
    df = pd.read_json(path_or_buf=file_path, lines=True)
    df = df[selected_columns]
    df = df.rename(columns={'utt': 'utt2','annot_utt' : 'annot_utt2'})
    grouped = df.groupby('id', as_index=False).agg({
        'utt2': ' '.join,  # Combine 'utt2' values with a space separator
        'annot_utt2': ' '.join  # Combine 'annot_utt2' values with a space separator
    })
    merged_df = pd.merge(en_df, grouped, on='id', how='inner')

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    file_name = file_name[:2]

    # Define the Excel file path in the 'output' folder
    excel_file_path = os.path.join(output_folder, f'en-{file_name}.xlsx')

    merged_df.to_excel(excel_file_path, index=False)

    print(f'Merged DataFrame columns: {merged_df.columns}')
    print(file_path)

    break