import ast
import pandas as pd

def parse_file(input_file):
    """
    Parse a file where each line is a dictionary-like string, cleans up the data,
    and returns a list of parsed dictionaries.
    """
    parsed_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            cleaned_line = line.strip().replace("u'", "'").replace('u"', '"')
            if cleaned_line:
                parsed_data.append(ast.literal_eval(cleaned_line))
    return parsed_data

def convert_to_parquet(input_file, output_file, process=False):

    parsed_data = parse_file(input_file)
    df = pd.DataFrame(parsed_data)
    
    if process:
        df["price"] = pd.to_numeric(df["price"], errors='coerce')
        df["metascore"] = pd.to_numeric(df["metascore"], errors='coerce')    
    df.to_parquet(output_file, index=False)
    print(f"DataFrame has been saved to '{output_file}'")

