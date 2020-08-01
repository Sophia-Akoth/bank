from datetime import datetime
class Account:
    

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan_amount = 0
        self.loan=[]
    def formatted_time(self):
        time=datetime.now()
        return time.strftime("%d/%m/%Y ,%H:%M:%S")
        



    def account_name(self,bank):
        self.bank=bank
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name
        )
        return name

    def deposit(self, amount):
        try:
            amount +1
        except TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot deposit zero or negative ")
        else:
            self.balance += amount
            datetime=self.formatted_time()
            deposit={"amount":amount,"time":datetime}
            self.deposits.append(deposit)
            print(
                "Dear{} ,You have deposited {} to your account at {} and your new balance is {}".format(
                    self.first_name,amount, datetime, self.balance
                )
            )

    def get_deposit_statement(self):
        for statement in self.deposits:
            amount=deposit['amount']
            statement=("You deposited{} on {}".format(amount , self.formatted_time))
            print(statement)

    def withdraw(self, amount):
        try:
            amount +1
        except TypeError:
            print("Please enter amount in figures")
        return
        
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You have insufficient balance ")
        else:
            self.balance -= amount
            datetime=self.formatted_time()
            withdrawal={"amount":amount,"time":time}
            self.withdrawals.append(withdrawal)
            print(
                "Dear{} ,You have withdrawn {} from your account at {} and your new balance is {}".format(
                    self.first_name,amount, datetime,self.balance
                )
            )
    

    def get_balance(self):
        return "The balance for {} is {}".format(
            self.account_name(), self.balance
        )
    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            amount=withdrawal['amount']
            timeDate=self.formatted_time
            statement=("You withdrew{} on {}".format(amount,timeDate))
            print(statement)

    def get_loan(self, amount):
        try:
            amount +10
        except TypeError:
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
            amount +10
        except TypeError:
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
            time=datetime.now()
            repayment={
                "time":time , "amount":amount}
            self.loan_repayments.append(repayment)
            print("You have repaid your loan with {},your balance is {}".format(amount,self.loan))
    def loan_repayment_statement(self):
                for repayment in self.loan_repayments:
                    time=repayment['time']
                    amount=repayment['amount']
                    formatted_time=self.formatted_time(time)
                    statement=("You have repaid your loan with {}. Your loan balance is {}".format(amount,formatted_time))
                    print(statement)


class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_number,bank):
        self.bank=bank
        super().__init__(first_name,last_name,phone_number)
    
class MobileMoneyAccount(Account):
    def __init__(self,first_name,last_name,phone_number,service_provider):
        self.service_provider=service_provider
        self.airtime=[]
        self.bill=[]
        self.send_money=[]
        super().__init__(first_name,last_name,phone_number)

    def buy_airtime(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You don't have enough balnce. Your balance is {}".format(self.balance))
        else:
                self.balance -= amount
                time=datetime.now()
                airtime={"time":time,"airtime":amount}
                self.airtime.append(airtime)
                print("You have bought airtime worth {} on {}".format(amount,self.formatted_time(time))) 
    def pay_bill(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return  
        if amount > self.balance:
            print("You don't have enough balance. Your balance is {}".format(self.balance))
        else:
            self.balance -= amount
            time=datetime.now()
            bill={"time":time,"airtime":amount}
            self.bill.append(bill)
            print("You have paid a bill worth {} on {}".format(amount, time))
    def send_money(self,amount):
        try:
            amount + 1
        except TypeError:
                print("Please enter the amount in figures")
                return
        if amount > self.balance:
                print("You don't have enought balance to send such kind of money. Your balance is {}".format(self.balance))
        else:
                self.balance -= amount
                time=datetime.now()
                money={"time":time,"airtime":amount}
                self.send_money.append(money)
                print("You have sent an amount worth {} on {}".format(amount,time) 
    def receive_money(self,amount):
        print("You have received {} on {}. Your balance is {}" .format(amount,self.balance,self.formatted_time))                  