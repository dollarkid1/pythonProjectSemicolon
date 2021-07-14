
class Account:
    def __init__(self, account_name, account_number, balance, pin):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def set_account_name(self, account_name):
        self.account_name = account_name

    def get_account_name(self):
        return self.account_name

    def create_account(self, account_number):
        self.account_number = account_number

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance


