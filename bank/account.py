from datetime import datetime


class BankAccount:
    # bank = "KCB" - class variable

    def __init__(self, first_name, last_name, bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan_amount = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name
        )
        return name

    def deposit(self, amount):
        if amount <= 0:
            print("The deposit is too low ")
        else:
            self.balance += amount
            date = datetime.now().strftime("%d, %B, %Y")
            time = datetime.now().strftime("%Hr:%Min:%Sec")
            statement = "On {} at {}, Ksh {} was deposited into {}".format(
                date, time, amount, self.account_name()
            )
            self.deposits.append(statement)
            print(
                "You have deposited Ksh {} to {}".format(
                    amount, self.account_name()
                )
            )

    def get_deposit_statement(self):
        for statement in self.deposits:
            print(statement)

    def withdraw(self, amount):
        if amount <= 0:
            print("You cannot withdraw an amount that's zero or less than zero")
        elif amount > self.balance:
            print("You have insufficient balance ")
        else:
            self.balance -= amount
            print(
                "You have withdrawn {} from {}".format(
                    amount, self.account_name()
                )
            )

    def get_balance(self):
        return "The balance for {} is {}".format(
            self.account_name(), self.balance
        )

    def get_loan(self, amount):
        if amount <= 0:
            print("You cannot borrow an an amount less or equal to zero")
        else:
            self.loan_amount += amount
            self.balance += amount
            print(
                "A loan of Ksh {} has been successfully deposited into {}. Your new account balance is {}".format(
                    amount, self.account_name(), self.balance
                )
            )

    def repay_loan(self, amount):
        if self.loan_amount == 0:
            print(
                "There is no unpaid loan for {}".format(self.account_name())
            )
        elif amount <= 0:
            print("You cannot repay a less than or a zero")
        elif self.balance < amount:
            print(
                "You do not have enough balance to pay that amount of your loan"
            )
        elif self.loan_amount < amount:
            loan = self.loan_amount
            extra = amount - loan
            self.balance -= self.loan_amount
            self.loan_amount = 0
            print(
                "You have completed paying your loan of Ksh {}. The extra Ksh {} has been deposited in your account".format(
                    loan, extra
                )
            )
        else:
            self.balance -= amount
            self.loan_amount -= amount
            if self.loan_amount > 0:
                print(
                    "You have successfully repaid Ksh {} part of your loan. Your remaining loan balance is Ksh {}".format(
                        amount, self.loan_amount
                    )
                )
            if self.loan_amount == 0:
                print(
                    "You have completed repayed your loan of Ksh {}".format(
                        amount
                    )
                )