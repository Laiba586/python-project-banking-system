class Account:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully!")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"Account({self.account_number}, {self.name}, {self.balance})"


class BankingSystem:
    def __init__(self, file_name="accounts.txt"):
        self.file_name = file_name
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Load accounts from the file into a list of Account objects."""
        accounts = []
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",")
                    accounts.append(Account(name, int(account_number), float(balance)))
        except FileNotFoundError:
            print("No existing account data found. Starting fresh.")
        return accounts

    def save_accounts(self):
        """Save all accounts back to the file."""
        with open(self.file_name, "w") as file:
            for account in self.accounts:
                file.write(f"{account.account_number},{account.name},{account.balance}\n")

    def create_account(self, name, initial_balance=0.0):
        account_number = len(self.accounts) + 1  # Simple auto-increment logic
        new_account = Account(name, account_number, initial_balance)
        self.accounts.append(new_account)
        self.save_accounts()
        print(f"Account created successfully! Account Number: {account_number}")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def perform_deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
            self.save_accounts()

    def perform_withdrawal(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
            self.save_accounts()

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                print(account)


# Main Execution
if __name__ == "__main__":
    banking_system = BankingSystem()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show All Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial deposit amount: "))
            banking_system.create_account(name, initial_balance)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            banking_system.perform_deposit(account_number, amount)
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            banking_system.perform_withdrawal(account_number, amount)
        elif choice == "4":
            banking_system.show_all_accounts()
        elif choice == "5":
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
