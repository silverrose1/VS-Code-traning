import pandas as pd
import re

def validate_email(email):
    """Validates an email address using a regular expression."""
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Slightly improved regex
    return re.match(regex, email) is not None

def main():
    """Reads a CSV, validates emails, adds index, and writes valid/invalid emails to files."""
    try:
        df = pd.read_csv("F:\Programming Installation\VS Code traning\Python Learning\Validate Emails\customers_export.csv", encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File 'customers_export.csv' not found.")
        return
    except pd.errors.ParserError:
        print("Error: Could not parse the CSV file. Check the format and encoding.")
        return

    if 'Email' not in df.columns:  # Check if 'Email' column exists
        print("Error: 'Email' column not found in CSV.")
        return
    if 'ID' not in df.columns:  # Check if 'ID' column exists
        print("Error: 'ID' column not found in CSV.")
        return

    df['Email Index'] = range(1, len(df) + 1)  # Add Email Index starting from 1

    invalid_emails = df[~df['Email'].apply(validate_email)]
    invalid_emails.to_csv("invalid_emails.csv", index=False)

    valid_emails = df[df['Email'].apply(validate_email)]
    valid_emails.to_csv("valid_emails.csv", index=False)

if __name__ == "__main__":
    main()

