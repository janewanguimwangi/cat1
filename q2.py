import pandas as pd

# Define the file paths
en_json = 'data/en-US.jsonl'
sw_json = 'data/sw-KE.jsonl'
de_json = 'data/de-DE.jsonl'

# Load the JSONL files into DataFrames
en_df = pd.read_json(en_json, lines=True)
sw_df = pd.read_json(sw_json, lines=True)
de_df = pd.read_json(de_json, lines=True)

# Define the column name and sort values
column_name = 'partition'
sort_values = ['test', 'train', 'dev']

# Create a dictionary to store the filtered DataFrames
filtered_dfs = {}

# Filter and save DataFrames for each sort value
for sort_value in sort_values:
    en_filtered = en_df[en_df[column_name] == sort_value]
    sw_filtered = sw_df[sw_df[column_name] == sort_value]
    de_filtered = de_df[de_df[column_name] == sort_value]

    # Define the output file paths
    en_output_file = f'output/q2/en-US-{sort_value}.jsonl'
    sw_output_file = f'output/q2/sw-KE-{sort_value}.jsonl'
    de_output_file = f'output/q2/de-DE-{sort_value}.jsonl'

    # Save the filtered DataFrames to new JSONL files
    en_filtered.to_json(en_output_file, orient='records', lines=True)
    sw_filtered.to_json(sw_output_file, orient='records', lines=True)
    de_filtered.to_json(de_output_file, orient='records', lines=True)