# main.py

from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions, validate_and_filter
import os

DATA_FILE = os.path.join("data", "sales_data.txt")


def main():
    print("Starting Sales Analytics System (Q2)...\n")

    raw_lines = read_sales_data(DATA_FILE)
    transactions = parse_transactions(raw_lines)

    valid, invalid_count, summary = validate_and_filter(
        transactions,
        region=None,        # example: "North"
        min_amount=None,    # example: 5000
        max_amount=None     # example: 100000
    )

    print("\nValidation Summary:")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
