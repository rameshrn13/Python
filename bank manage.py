class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}"

def main():
    accounts = []

    while True:
        print("\nBank Management System Menu:")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            new_account = BankAccount(account_number, account_holder)
            accounts.append(new_account)
            print("Account created successfully.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the deposit amount: "))
            account = find_account(accounts, account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            account = find_account(accounts, account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = find_account(accounts, account_number)
            if account:
                print(account)
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

if __name__ == "__main__":
    main()