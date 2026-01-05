from datetime import datetime
from utils.data_processor import region_wise_sales

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
