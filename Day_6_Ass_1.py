class BankAccount:

    def __init__(self, name, balance):
        self.owner_name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount successfully deposited. Current balance is Rs. {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance is Rs. {self.balance}.")
        else:
            print(f"Transaction could not be performed due to insufficient funds.")

ba1 = BankAccount("Amit Pathak", 30000)
ba1.deposit(4000)
ba1.withdraw(20000)
ba1.withdraw(20000)
print("-"*50)

ba2 = BankAccount("Bhavisha Kapadia", 10000)
ba2.withdraw(12000)
ba2.deposit(5000)
ba2.withdraw(12000)