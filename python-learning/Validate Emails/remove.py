import pandas as pd

def remove_duplicates(filepath, output_path):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return
    except pd.errors.ParserError:
        print(f"Error parsing '{filepath}'. Check the file format.")
        return

    if df.empty:
        print(f"The file '{filepath}' is empty.")
        return

    #Remove exact duplicates
    # df.drop_duplicates(subset=df.columns.tolist(), keep='first', inplace=True)
    #Remove any rows where a value is duplicated in any column.
    df.drop_duplicates(inplace=True)
    df.to_csv(output_path, index=False)
    print(f"Duplicates removed and saved to '{output_path}'.")

def main():
    filepath = "3.csv"
    output_path = "4.csv"
    remove_duplicates(filepath, output_path)

if __name__ == "__main__":
    main()
