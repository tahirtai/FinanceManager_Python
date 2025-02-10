import json 

class Transaction:
    def __init__(self, amount, category, transaction_type):
        
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type 

    def __str__(self):
        return f"{self.transaction_type.capitalize()}: {self.amount} - {self.category}"


    
class FinanceManager:
    
    FILE_NAME = "transactions.json"

    def __init__(self):
        self.transactions = []
        self.load_transactions() 

    def save_transactions(self):
        with open(self.FILE_NAME, "w") as file: 
            json.dump([t.__dict__ for t in self.transactions], file)  

    def load_transactions(self):
        try:
            with open(self.FILE_NAME, "r") as file:  
                data = json.load(file) 
                self.transactions = [Transaction(**item) for item in data]  
        except (FileNotFoundError, json.JSONDecodeError):  
            pass  

    
    def add_transaction(self, amount, category, transaction_type):
        if amount <= 0:
            print(" Amount must be positive!")
            return
        
        transaction = Transaction(amount, category, transaction_type)
        self.transactions.append(transaction)
        self.save_transactions()  
        print(" Transaction added successfully!")


    def view_transactions(self):
        if not self.transactions:
            print(" No transactions found!")
            return
        
        print("\n Transaction History:")
        for i, transaction in enumerate(self.transactions, 1):
            print(f"{i}. {transaction}")

    def calculate_balance(self):
        balance = sum(t.amount if t.transaction_type == "income" else -t.amount for t in self.transactions)
        return balance

    def delete_transaction(self):
        if not self.transactions:
            print(" No transactions to delete!!")
            return

        self.view_transactions() 

        try:
            index = int(input("Enter the transaction number to delete: ")) - 1  
            if 0 <= index < len(self.transactions): 
                removed_transaction = self.transactions.pop(index)  
                self.save_transactions() 
                print(f" Deleted: {removed_transaction}")
            else:
                print(" Invalid transaction number!")
        except ValueError:
            print(" Please enter a valid number!")


def main():
    finance_manager = FinanceManager()
    
    while True:
        print("\n===== PERSONAL FINANCE MANAGER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Check Balance")
        print("5. Delete Transaction")
        print("6. Exit")
        
        choice = input("Choose an option : ")

        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                category = input("Enter income source: ")
                finance_manager.add_transaction(amount, category, "income")
            except ValueError:
                print(" Invalid amount. Please enter a number.")
        
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense reason : ")
                finance_manager.add_transaction(amount, category, "expense")
            except ValueError:
                print(" Invalid amount. Please enter a number.")
        
        elif choice == "3":
            finance_manager.view_transactions()
        
        elif choice == "4":
            balance = finance_manager.calculate_balance()
            print(f"\n Your Current Balance: {balance}")

        elif choice == "5":
            finance_manager.delete_transaction()  

        elif choice == "6":
            print(" Exiting...")
            break
        
        else:
            print(" Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()





