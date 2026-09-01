"""
Retail Sales and Consumer Behaviour Analysis System
Requirement RQ1: Customer Spending Segmentation

Module : COMP 30010.1 - Software Quality Assurance
Author : Mohammed Albalushi
"""


def segment_customers(transactions, high_value_threshold, premium_threshold):
    """
    Classify each transaction into a spending segment and accumulate revenue.

    transactions          : list of dicts, each {"customer_id": str, "amount": float}
    high_value_threshold  : minimum amount for a transaction to be High-Value
    premium_threshold     : minimum amount for a transaction to be Premium

    Returns a dict holding the three segment lists and the total revenue.
    """

    # NODE 1 - initialisation
    premium_customers = []
    high_value_customers = []
    regular_customers = []
    total_revenue = 0
    transaction_count = 0

    # NODE 2 - loop control
    for record in transactions:

        # NODE 3 - read the amount and accumulate revenue
        amount = record["amount"]
        total_revenue = total_revenue + amount
        transaction_count = transaction_count + 1

        # NODE 4 - first decision
        if amount >= high_value_threshold:

            # NODE 5 - second decision
            if amount >= premium_threshold:
                # NODE 6
                premium_customers.append(record["customer_id"])
            else:
                # NODE 7
                high_value_customers.append(record["customer_id"])
            # NODE 8 - inner merge
        else:
            # NODE 9
            regular_customers.append(record["customer_id"])
        # NODE 10 - outer merge, loop back to NODE 2

    # NODE 11 - exit
    return {
        "premium": premium_customers,
        "high_value": high_value_customers,
        "regular": regular_customers,
        "total_revenue": total_revenue,
        "transaction_count": transaction_count,
    }


if __name__ == "__main__":
    sample_transactions = [
        {"customer_id": "C001", "amount": 45.0},
        {"customer_id": "C002", "amount": 250.0},
        {"customer_id": "C003", "amount": 900.0},
        {"customer_id": "C004", "amount": 120.0},
    ]

    result = segment_customers(sample_transactions, 100, 500)

    print("Premium     :", result["premium"])
    print("High-Value  :", result["high_value"])
    print("Regular     :", result["regular"])
    print("Total Revenue:", result["total_revenue"])
