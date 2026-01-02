# utils/data_processor.py

def clean_and_process_data(lines):
    """
    Cleans, validates, and processes raw sales data lines.
    Returns cleaned records.
    """

    total_records = 0
    invalid_records = 0
    cleaned_records = []

    header_skipped = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Skip header
        if not header_skipped:
            header_skipped = True
            continue

        total_records += 1
        parts = line.split('|')

        # Must have 8 columns
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
        if not transaction_id.startswith("T"):
            invalid_records += 1
            continue

        if not customer_id or not region:
            invalid_records += 1
            continue

        # Clean quantity
        try:
            quantity = int(quantity.replace(',', ''))
            if quantity <= 0:
                invalid_records += 1
                continue
        except ValueError:
            invalid_records += 1
            continue

        # Clean unit price
        try:
            unit_price = float(unit_price.replace(',', ''))
            if unit_price <= 0:
                invalid_records += 1
                continue
        except ValueError:
            invalid_records += 1
            continue

        # Clean product name
        product_name = product_name.replace(',', '')

        # Calculate revenue
        revenue = quantity * unit_price

        cleaned_record = (
            f"{transaction_id}|{date}|{product_id}|{product_name}|"
            f"{quantity}|{unit_price:.2f}|{customer_id}|{region}|{revenue:.2f}"
        )

        cleaned_records.append(cleaned_record)

    # Print summary
    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {invalid_records}")
    print(f"Valid records after cleaning: {len(cleaned_records)}")

    return cleaned_records
