from datetime import datetime
from utils.data_processor import region_wise_sales
from utils.data_processor import top_selling_products
from utils.data_processor import customer_analysis



def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive formatted text report
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # HEADER SECTION
        f.write("=" * 44 + "\n")
        f.write("          SALES ANALYTICS REPORT\n")
        f.write(f"    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"    Records Processed: {len(transactions)}\n")
        f.write("=" * 44 + "\n\n")



        # OVERALL SUMMARY
        total_revenue = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
        total_transactions = len(transactions)
        avg_order_value = total_revenue / total_transactions if total_transactions else 0

        dates = [t['Date'] for t in transactions]
        start_date = min(dates)
        end_date = max(dates)

        f.write("OVERALL SUMMARY\n")
        f.write("-" * 44 + "\n")
        f.write(f"Total Revenue:        ₹{total_revenue:,.2f}\n")
        f.write(f"Total Transactions:   {total_transactions}\n")
        f.write(f"Average Order Value:  ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range:           {start_date} to {end_date}\n\n")


        # REGION-WISE PERFORMANCE
        region_data = region_wise_sales(transactions)

        f.write("REGION-WISE PERFORMANCE\n")
        f.write("-" * 44 + "\n")
        f.write(f"{'Region':<10}{'Sales':<15}{'% of Total':<12}{'Transactions'}\n")

        for region, info in region_data.items():
            f.write(
                f"{region:<10}"
                f"₹{info['total_sales']:,.2f}  "
                f"{info['percentage']:<12}%"
                f"{info['transaction_count']}\n"
            )

        f.write("\n")


        # TOP 5 PRODUCTS
        top_products = top_selling_products(transactions, n=5)

        f.write("TOP 5 PRODUCTS\n")
        f.write("-" * 44 + "\n")
        f.write(f"{'Rank':<6}{'Product Name':<25}{'Qty Sold':<10}{'Revenue'}\n")

        for idx, product in enumerate(top_products, start=1):
            name, qty, revenue = product
            f.write(
                f"{idx:<6}"
                f"{name:<25}"
                f"{qty:<10}"
                f"₹{revenue:,.2f}\n"
            )

        f.write("\n")

        # TOP 5 CUSTOMERS
        customer_stats = customer_analysis(transactions)

        f.write("TOP 5 CUSTOMERS\n")
        f.write("-" * 44 + "\n")
        f.write(f"{'Rank':<6}{'Customer ID':<15}{'Total Spent':<15}{'Orders'}\n")

        for idx, (cust_id, info) in enumerate(customer_stats.items(), start=1):
            if idx > 5:
                break

            f.write(
                f"{idx:<6}"
                f"{cust_id:<15}"
                f"₹{info['total_spent']:,.2f}  "
                f"{info['purchase_count']}\n"
            )

        f.write("\n")


