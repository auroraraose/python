import csv
import random

USER_FILE = "users.csv"
TRANSACTION_FILE = "transactions.csv"

class BankAccount:
    def __init__(self, initial_deposit, card_number=None, password=None):
        
        self.card_number = card_number or ''.join([str(random.randint(0, 9)) for _ in range(16)])
        self.password = password or ''.join([str(random.randint(0, 9)) for _ in range(8)])
        self.balance = initial_deposit

        if not card_number:
            self.record_transaction("Deposit", initial_deposit)

    def show_balance(self):
        print(f"Balance: {self.balance:.2f}")

    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount")
            return
        self.balance += amount
        self.update_user_balance()
        self.record_transaction("Deposit", amount)
        print(f"Amount deposited: {amount:.2f}")
        self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount < 0:
            print("Amount cannot be less than 0")
        else:
            self.balance -= amount
            self.update_user_balance()
            self.record_transaction("Withdrawal", amount)
            print(f"Amount debited: {amount:.2f}")
            self.show_balance()

    def record_transaction(self, transaction_type, amount):
        
        with open(TRANSACTION_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.card_number, transaction_type, amount])

    def show_transaction_history(self):
       
        print("\nTransaction History:")
        with open(TRANSACTION_FILE, "r") as f:
            reader = csv.reader(f)
            found = False
            for row in reader:
                if row and row[0] == self.card_number:
                    print(f"{row[1]}: {row[2]}")
                    found = True
            if not found:
                print("No transactions found.")

    def update_user_balance(self):

        users = []
        with open(USER_FILE, "r") as f:
            reader = csv.reader(f)
            users = list(reader)

        for row in users:
            if row and row[0] == self.card_number:
                row[4] = str(self.balance)

        with open(USER_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(users)
