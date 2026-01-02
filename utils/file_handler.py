# utils/file_handler.py

def read_sales_data(file_path):
    """
    Reads the sales data file and returns a list of lines.
    """
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def write_enriched_data(file_path, data):
    """
    Writes cleaned and enriched sales data to a file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for record in data:
                file.write(record + '\n')
    except Exception as e:
        print(f"Error writing enriched data: {e}")


def write_sales_report(file_path, report_lines):
    """
    Writes the sales report to a file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in report_lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"Error writing sales report: {e}")
