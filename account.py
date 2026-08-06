class Account:
    def __init__(self, account_no, details):
        self.account_no = account_no
        self.name = details["name"]
        self.pin = details["pin"]
        self.balance = details["balance"]
        self.transactions = details["transactions"]

    def to_dict(self):
        return {
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }