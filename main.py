# main.py

from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions,
    validate_and_filter,
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products
)
from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data
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

    # Find peak salesday
    print("\nPeak Sales Day:")
    peak_day = find_peak_sales_day(valid)
    print(peak_day)

    # Test Low Performing Products
    print("\nTesting Low Performing Products:")
    low_products = low_performing_products(valid, threshold=10)
    if low_products:
        for product in low_products:
            print(product)
    else:
        print("No low performing products found.")

    # -----------------------------
    # Q4: API Integration – Step 3.1 (a)
    # -----------------------------
    print("\nTesting API Fetch:")
    api_products = fetch_all_products()
    print("Number of products fetched:", len(api_products))

    print("\nFirst 3 API Products:")
    for p in api_products[:3]:
        print(p)

    # -----------------------------
    # Q4: API Integration – Step 3.1 (b)
    # -----------------------------

    print("\nFetching products from DummyJSON API...")
    api_products = fetch_all_products()   # ✅ THIS LINE WAS MISSING

    print("Total products fetched:", len(api_products))

    print("\nTesting Product Mapping:")
    product_mapping = create_product_mapping(api_products)

    print("Total mapped products:", len(product_mapping))

    count = 0
    for pid, info in product_mapping.items():
        print(pid, info)
        count += 1
        if count == 3:
           break



    # -----------------------------
    # Q4: API Integration – Step 3.2
    # -----------------------------


    print("\nTesting enrichment of first 5 transactions:")
    enriched_data = enrich_sales_data(transactions[:5], product_mapping)
    for t in enriched_data:
        print(t)




if __name__ == "__main__":
    main()
