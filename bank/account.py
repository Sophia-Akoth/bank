from datetime import datetime
class BankAccount:
    

    def __init__(self, first_name, last_name, bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan_amount = 0
        self.loan=[]
    def current_time(self):
        time=datetime.now()
        time_formatted=time.strftime("%d/%m/Y ,%H:%M:%S")
        return time_formatted



    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name
        )
        return name

    def deposit(self, amount):
        try:
            amount +1
        except:TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot deposit zero or negative ")
        else:
            self.balance += amount
            datetime=self.get current_time()
            transaction_details={"amount":amount,"date":datetime}
            self.deposits.append(transaction_details)
            print(
                "Dear{} ,You have deposited {} to your account at {} and your new balance is {}".format(
                    self.first_name,amount, datetime self.balance
                )
            )

    def get_deposit_statement(self):
        for statement in self.deposits:
            print("On"statement['date'],",You deposited KES",statement['amount'])

    def withdraw(self, amount):
        try:
            amount +1
        except:TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You have insufficient balance ")
        else:
            self.balance -= amount
            datetime=self.get current_time()
            transaction_details={"amount":amount,"date":datetime}
            self.withdrawals.append(transaction_details)
            print(
                "Dear{} ,You have withdrawn {} from your account at {} and your new balance is {}".format(
                    self.first_name,amount, datetime self.balance
                )
            )
    

    def get_balance(self):
        return "The balance for {} is {}".format(
            self.account_name(), self.balance
        )
    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            print(("On"withdrawal['date'],",You withdrew KES",withdrawal['amount'])

    def get_loan(self, amount):
        try:
            amount +1
        except:TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot request a loan for that amount")
        else:
            self.loan_amount += amount
            self.balance += amount
            print(
                "A loan of Ksh {} has been successfully deposited into {}. Your new account balance is {}".format(
                    amount, self.account_name(), self.balance
                )
            )

    def repay_loan(self, amount):
        try:
            amount +1
        except:TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot repay with that amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print(
                "Your loan is {},please use an amount less or equal".format(self.loan)
            )
        else:
            self.loan > amount
            print("You have repaid your loan with {},your balance is {}".format(amount,self.loan))
acc1=BankAccount("Sophia","Akoth",0722456789)
acc2=BankAccount("Sophia","Akoth",0722456789)
acc1.deposit(1000)
acc2.deposit(2000)
acc1.withdraw(100)
acc2.withdraw(500)
            