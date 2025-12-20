class BankAccount:
    def __init__(self,balance):
        self.balance= balance


    def deposit(self, amount):
        self.balance += amount
        print("balance after deposit:",self.balance)

    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
            print("Balance after withdraw",self.balance)
        else:
            print("insufficient balance")

acc=BankAccount(5000)
acc.deposit(200)
acc.withdraw(500)
