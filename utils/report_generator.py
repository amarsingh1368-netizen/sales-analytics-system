from datetime import datetime

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
