import random

store = {}

def makeAcc():
    name = input("Enter your name: ")
    contact = input("Enter contact details: ")
    initialDeposit = float(input("Enter initial deposit amount: "))
    
    if initialDeposit < 0:
        print("Initial deposit cannot be negative.")
        return
    
    cardNumber = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    
    store[cardNumber] = {
        "name": name,
        "contact": contact,
        "balance": initialDeposit,
        "password": password,
        "transactions": [("Deposit", initialDeposit)]
    }
    print(f"Account created successfully!\nCard Number: {cardNumber}\nPassword: {password}\nBalance: {initialDeposit:.2f}")

def showBal():
    cardNumber = input("Enter card number: ")
    if cardNumber in store:
        print(f"Balance: {store[cardNumber]['balance']:.2f}")
    else:
        print("Invalid card number.")

def deposit():
    cardNumber = input("Enter card number: ")
    if cardNumber in store:
        amount = float(input("Enter the amount to deposit: "))
        
        if amount < 0:
            print("Invalid amount")
        else:
            store[cardNumber]["balance"] += amount
            store[cardNumber]["transactions"].append(("Deposit", amount))
            print(f"Amount deposited: {amount:.2f}")
            print(f"Current balance: {store[cardNumber]['balance']:.2f}")
    else:
        print("Invalid card number.")
        
def transHistory():
    cardNumber = input("Enter card number: ")
    if cardNumber in store:
        print("\nTransaction History:")
        for transaction in store[cardNumber]["transactions"]:
            print(f"{transaction[0]}: {transaction[1]:.2f}")
    else:
        print("Invalid card number.")


def withdrawl():
    cardNumber = input("Enter card number: ")
    if cardNumber in store:
        amount = float(input("Withdrawal Amount: "))
        
        if amount > store[cardNumber]["balance"]:
            print("Insufficient balance")
        elif amount < 0:
            print("Amount cannot be less than 0")
        else:
            store[cardNumber]["balance"] -= amount
            store[cardNumber]["transactions"].append(("Withdrawal", amount))
            print(f"Amount debited: {amount:.2f}")
            print(f"Current balance: {store[cardNumber]['balance']:.2f}")
    else:
        print("Invalid card number.")

isRun = True
while isRun:
    print("\n0. Add your details")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    if choice == "0":
        makeAcc()
    elif choice == "1":
        showBal()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdrawl()
    elif choice == "4":
        transHistory()
    elif choice == "5":
        isRun = False
    else:
        print("Invalid choice, please enter between 0-4.")
