# utils/data_processor.py

def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """
    transactions = []

    for line in raw_lines:
        parts = line.split('|')

        # Skip rows with incorrect number of fields
        if len(parts) != 8:
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

        # Clean product name (remove commas)
        product_name = product_name.replace(',', '')

        # Clean numeric fields
        try:
            quantity = int(quantity.replace(',', ''))
            unit_price = float(unit_price.replace(',', ''))
        except ValueError:
            continue

        transactions.append({
            'TransactionID': transaction_id,
            'Date': date,
            'ProductID': product_id,
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'CustomerID': customer_id,
            'Region': region
        })

    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters
    """

    valid_transactions = []
    invalid_count = 0

    # Validation
    for t in transactions:
        if (
            t['Quantity'] <= 0 or
            t['UnitPrice'] <= 0 or
            not t['TransactionID'].startswith('T') or
            not t['ProductID'].startswith('P') or
            not t['CustomerID'].startswith('C') or
            not t['Region']
        ):
            invalid_count += 1
            continue

        valid_transactions.append(t)

    # Display available regions
    regions = sorted(set(t['Region'] for t in valid_transactions))
    print(f"Available regions: {', '.join(regions)}")

    # Display transaction amount range
    amounts = [t['Quantity'] * t['UnitPrice'] for t in valid_transactions]
    print(f"Transaction amount range: {min(amounts):.2f} - {max(amounts):.2f}")

    filtered = valid_transactions[:]
    filtered_by_region = 0
    filtered_by_amount = 0

    # Filter by region
    if region:
        filtered_by_region = sum(1 for t in filtered if t['Region'] != region)
        filtered = [t for t in filtered if t['Region'] == region]
        print(f"After region filter ({region}): {len(filtered)} records")

    # Filter by min amount
    if min_amount is not None:
        removed = [t for t in filtered if t['Quantity'] * t['UnitPrice'] < min_amount]
        filtered_by_amount += len(removed)
        filtered = [t for t in filtered if t['Quantity'] * t['UnitPrice'] >= min_amount]
        print(f"After min amount filter ({min_amount}): {len(filtered)} records")

    # Filter by max amount
    if max_amount is not None:
        removed = [t for t in filtered if t['Quantity'] * t['UnitPrice'] > max_amount]
        filtered_by_amount += len(removed)
        filtered = [t for t in filtered if t['Quantity'] * t['UnitPrice'] <= max_amount]
        print(f"After max amount filter ({max_amount}): {len(filtered)} records")

    summary = {
        'total_input': len(transactions),
        'invalid': invalid_count,
        'filtered_by_region': filtered_by_region,
        'filtered_by_amount': filtered_by_amount,
        'final_count': len(filtered)
    }

    return filtered, invalid_count, summary


def calculate_total_revenue(transactions):
    """
    Calculates total revenue from all transactions

    Returns: float (total revenue)
    """
    total_revenue = 0.0

    for txn in transactions:
        total_revenue += txn['Quantity'] * txn['UnitPrice']

    return round(total_revenue, 2)

