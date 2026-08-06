from database import save_data
from transactions import add_transaction


class Bank:
    def __init__(self, data, account):
        self.data = data
        self.account = account

    def save(self):
        self.data[self.account.account_no] = self.account.to_dict()
        save_data(self.data)

    def check_balance(self):
        print("\n" + "=" * 35)
        print("CURRENT BALANCE")
        print("=" * 35)
        print(f"Account Holder : {self.account.name}")
        print(f"Balance        : ₹{self.account.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                print("❌ Invalid amount.")
                return

            self.account.balance += amount
            add_transaction(self.account, "Deposit", amount)

            self.save()

            print("✅ Amount deposited successfully.")
            print(f"New Balance : ₹{self.account.balance}")

        except ValueError:
            print("❌ Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("❌ Invalid amount.")
                return

            if amount > self.account.balance:
                print("❌ Insufficient Balance.")
                return

            self.account.balance -= amount
            add_transaction(self.account, "Withdraw", amount)

            self.save()

            print("✅ Withdrawal successful.")
            print(f"Remaining Balance : ₹{self.account.balance}")

        except ValueError:
            print("❌ Please enter a valid amount.")

    def change_pin(self):
        old_pin = input("Enter Current PIN: ")

        if old_pin != self.account.pin:
            print("❌ Incorrect Current PIN.")
            return

        new_pin = input("Enter New PIN: ")
        confirm_pin = input("Confirm New PIN: ")

        if new_pin != confirm_pin:
            print("❌ PINs do not match.")
            return

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("❌ PIN must be exactly 4 digits.")
            return

        self.account.pin = new_pin
        self.save()

        print("✅ PIN changed successfully.")