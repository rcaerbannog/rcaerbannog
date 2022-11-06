class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def displayBalance(self):
        print ("Account balance: " + str(round(self.balance, 2)))

    def deposit(self, amount):
        if (amount < 0): print ("ERROR: Cannot deposit negative amounts of money.")
        else: self.balance += amount

    def withdrawl(self, amount):
        if (amount < 0): print ("ERROR: Cannot withdraw negative amounts of money.")
        else: self.balance -= amount
#END BankAccount

class InterestAccount(BankAccount):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def addInterest(self):
        self.balance *= (1 + self.interest_rate)
#END InterestAccount

#Main
myAccount = InterestAccount("Alexander Li", "19836892", 0, 0.1)
myAccount.displayBalance()
myAccount.deposit(100)
myAccount.displayBalance()
myAccount.addInterest()
myAccount.displayBalance()
