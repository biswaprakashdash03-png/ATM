from datetime import datetime


def add_transaction(account, transaction_type, amount):
    """
    Add a transaction to the account history.
    """

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    account.transactions.append(transaction)


def show_transactions(account):
    """
    Display all transactions of the account.
    """

    print("\n" + "=" * 45)
    print("        TRANSACTION HISTORY")
    print("=" * 45)

    if len(account.transactions) == 0:
        print("No transactions found.")
        return

    for i, transaction in enumerate(account.transactions, start=1):
        print(f"\nTransaction {i}")
        print("-" * 30)
        print(f"Type   : {transaction['type']}")
        print(f"Amount : ₹{transaction['amount']}")
        print(f"Date   : {transaction['date']}")