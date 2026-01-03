# main.py

from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions,
    validate_and_filter,
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend
)
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


    print("\n========== Q3 TESTING ==========\n")

    # Total Revenue
    total_revenue = calculate_total_revenue(valid)
    print(f"Total Revenue: {total_revenue}")

    # Region-wise Sales
    print("\nRegion-wise Sales:")
    region_sales = region_wise_sales(valid)
    for region, data in region_sales.items():
        print(region, data)

    # Top Selling Products
    print("\nTop Selling Products:")
    for product in top_selling_products(valid):
        print(product)

    # Customer Analysis (show top 5 only)
    print("\nTop Customers:")
    customers = customer_analysis(valid)
    count = 0
    for cid, info in customers.items():
        print(cid, info)
        count += 1
        if count == 5:
            break

    # Daily Sales Trend (first 5 days)
    print("\nDaily Sales Trend:")
    daily_trend = daily_sales_trend(valid)
    count = 0
    for date, info in daily_trend.items():
        print(date, info)
        count += 1
        if count == 5:
            break


if __name__ == "__main__":
    main()
