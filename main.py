from database import load_data

data = load_data()

print("=" * 35)
print("      ATM BANKING SYSTEM")
print("=" * 35)

account_no = input("Enter Account Number: ")
pin = input("Enter PIN: ")

if account_no in data:
    if data[account_no]["pin"] == pin:
        print("\n✅ Login Successful")
        print("Welcome,", data[account_no]["name"])
    else:
        print("\n❌ Wrong PIN")
else:
    print("\n❌ Account Not Found")