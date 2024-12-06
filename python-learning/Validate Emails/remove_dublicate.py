import pandas as pd

def remove_duplicates(file1_path, file2_path, output_path):
    """Removes rows from file1 that exist in file2 and saves the result to file3."""
    try:
        df1 = pd.read_csv(file1_path)
        df2 = pd.read_csv(file2_path)
    except (FileNotFoundError, pd.errors.ParserError) as e:  # Combine exception handling
        print(f"Error reading or parsing CSV: {e}")
        return

    if df1.empty or df2.empty:
        print("One or both input files are empty.")
        df1.to_csv(output_path, index=False)
        return 0

    original_len = len(df1)

    df3 = df1.merge(df2, on=list(df1.columns), how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)
    df3.to_csv(output_path, index=False)

    rows_removed = original_len - len(df3)
    print(f"Number of rows removed from file 1: {rows_removed}")
    return rows_removed


def main():
    file1_path = "valid_emails.csv"  # Example: Replace with your actual file paths
    file2_path = "invalid_emails.csv"
    output_path = "3.csv"
    remove_duplicates(file1_path, file2_path, output_path)

if __name__ == "__main__":
    main()

