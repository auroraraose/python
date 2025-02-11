import csv
from bank import BankAccount 

USER_FILE = "users.csv"

class User:
    def __init__(self, name, contact, initial_deposit, card_number=None, password=None):
        self.name = name
        self.contact = contact
        self.account = BankAccount(initial_deposit, card_number, password)

    def save_to_csv(self):
        with open(USER_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.account.card_number, self.name, self.contact, self.account.password, self.account.balance])

    @staticmethod
    def get_user(card_number):
        with open(USER_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == card_number:
                    return User(row[1], row[2], float(row[4]), row[0], row[3])
        return None

    def show_details(self):
        print(f"Name: {self.name}\nContact: {self.contact}\nCard Number: {self.account.card_number}")
