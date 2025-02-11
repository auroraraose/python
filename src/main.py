from user import User

def main():
    def create_user():
        name = input("Enter your name: ")
        contact = input("Enter contact details: ")
        initial_deposit = float(input("Enter initial deposit amount: "))

        user = User(name, contact, initial_deposit)
        user.save_to_csv()

        print(f"Account created successfully!\nCard Number: {user.account.card_number}\nPassword: {user.account.password}\nBalance: {user.account.balance:.2f}")

    def get_user():
        card_number = input("Enter card number: ")
        return User.get_user(card_number)

    def show_balance():
        user = get_user()
        if user:
            user.account.show_balance()
        else:
            print("Invalid card number.")

    def deposit_money():
        user = get_user()
        if user:
            amount = float(input("Enter the amount to deposit: "))
            user.account.deposit(amount)
        else:
            print("Invalid card number.")

    def withdraw_money():
        user = get_user()
        if user:
            amount = float(input("Withdrawal Amount: "))
            user.account.withdraw(amount)
        else:
            print("Invalid card number.")

    def transaction_history():
        user = get_user()
        if user:
            user.account.show_transaction_history()
        else:
            print("Invalid card number.")

    while True:
        print("\n0. Create Account")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "0":
            create_user()
        elif choice == "1":
            show_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please enter between 0-5.")

if __name__ == "__main__":
    main()
