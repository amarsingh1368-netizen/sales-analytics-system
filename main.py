# main.py

from utils.file_handler import read_sales_data, write_enriched_data
from utils.data_processor import clean_and_validate_data
import os

DATA_FILE = os.path.join("data", "sales_data.txt")
OUTPUT_FILE = os.path.join("output", "enriched_sales_data.txt")


def main():
    print("Starting Sales Analytics System...\n")

    raw_lines = read_sales_data(DATA_FILE)
    valid_records = clean_and_validate_data(raw_lines)

    write_enriched_data(OUTPUT_FILE, valid_records)

    print("\nQ1 Processing Complete.")
    print("Cleaned data written to output/enriched_sales_data.txt")


if __name__ == "__main__":
    main()
