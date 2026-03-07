"""
--------------------------------------------------
SIMPLE BANK PROGRAM
Practice:
✔ Variables
✔ User Input
✔ Conditions
✔ Formatting
✔ Functions
✔ Dunder Method
--------------------------------------------------
"""


# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def show_balance(balance):
    print(f"\n💰 Your balance is: ${balance:.2f}")


def deposite():
    amount = float(input("Enter the deposit amount: "))

    if amount <= 0:
        print("❌ Enter amount greater than 0.")
        return 0   # FIXED: Return 0 instead of None
    else:
        print("✅ Amount deposited successfully.")
        return amount


def withdrwa(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return 0   # FIXED
    elif amount > balance:
        print("❌ Insufficient balance.")
        return 0   # FIXED
    else:
        print("✅ Withdrawal successful.")
        return amount


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n" + "=" * 50)
        print("🏦 Welcome to the Bank")
        print("=" * 50)

        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")
        print("-" * 50)

        option = int(input("Enter your choice (1-4): "))

        if option == 1:
            show_balance(balance)

        elif option == 2:
            balance += deposite()

        elif option == 3:
            amount = withdrwa(balance)
            balance -= amount  

        elif option == 4:
            is_running = False
            print("👋 Thank you for using our bank!")

        else:
            print("❌ Enter a valid option (1-4).")


# --------------------------------------------------
# DUNDER METHOD
# --------------------------------------------------

if __name__ == "__main__":
    main()