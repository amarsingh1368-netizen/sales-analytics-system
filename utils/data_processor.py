# utils/data_processor.py

def clean_and_validate_data(raw_lines):
    """
    Parses, cleans, and validates raw sales data
    Prints required validation summary
    """

    total_records = 0
    invalid_records = 0
    valid_records = []

    for line in raw_lines:
        total_records += 1
        parts = line.split('|')

        # Must have exactly 8 fields
        if len(parts) != 8:
            invalid_records += 1
            continue

        (
            transaction_id,
            date,
            product_id,
            product_name,
            quantity,
            unit_price,
            customer_id,
            region
        ) = parts

        # Validation rules
        if not transaction_id.startswith('T'):
            invalid_records += 1
            continue

        if not customer_id or not region:
            invalid_records += 1
            continue

        # Clean product name
        product_name = product_name.replace(',', '')

        # Clean numeric fields
        try:
            quantity = int(quantity.replace(',', ''))
            unit_price = float(unit_price.replace(',', ''))
        except ValueError:
            invalid_records += 1
            continue

        if quantity <= 0 or unit_price <= 0:
            invalid_records += 1
            continue

        valid_records.append({
            'TransactionID': transaction_id,
            'Date': date,
            'ProductID': product_id,
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'CustomerID': customer_id,
            'Region': region
        })

    # REQUIRED OUTPUT
    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {invalid_records}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records
