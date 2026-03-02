accounts = {}

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    
    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }
    
    print("Account created successfully!\n")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter deposit amount: "))
        accounts[acc_no]["balance"] += amount
        print("Amount deposited successfully!\n")
    else:
        print("Account not found!\n")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter withdraw amount: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Amount withdrawn successfully!\n")
        else:
            print("Insufficient balance!\n")
    else:
        print("Account not found!\n")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"], "\n")
    else:
        print("Account not found!\n")

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using Banking System")
        break
    else:
        print("Invalid choice!\n")

