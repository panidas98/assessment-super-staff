def aggregate_sales(transactions):
    """
    Takes a list of sales transactions and returns the total quantity sold per product.

    Each transaction is a dict with 'product' and 'quantity' keys.
    If a product appears more than once, the quantities just get summed up.
    """
    totals = {}

    for tx in transactions:
        product = tx["product"]
        quantity = tx["quantity"]

        # if we've seen this product before, add to the running total
        # otherwise start it from scratch
        if product in totals:
            totals[product] += quantity
        else:
            totals[product] = quantity

    return totals


# --- quick sanity check ---
if __name__ == "__main__":
    transactions = [
        {"product": "apple", "quantity": 10},
        {"product": "banana", "quantity": 5},
        {"product": "apple", "quantity": 3},
        {"product": "orange", "quantity": 8},
        {"product": "banana", "quantity": 2},
    ]

    result = aggregate_sales(transactions)
    print(result)
    # expected: {'apple': 13, 'banana': 7, 'orange': 8}

    assert result == {"apple": 13, "banana": 7, "orange": 8}, "Something went wrong"
    print("All checks passed.")
