class Bank:
    accounts = []

    def __init__(self, bank_name, pin):
        self.pin = pin
        self.bank_name = bank_name

    def register(self, first_name, last_name, date_of_birth, phone_number):
        pass

    def login(self, account_number, pin):
        pass

    def deposit(self, balance, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, balance, pin, amount):
        pass
        if self.pin == pin:
            if balance >= amount:
                balance -= amount
        else:
            print("Invalid Pin")

    def transfer(self, balance, pin, amount):
        if self.pin == pin:
            if balance >= amount:
                balance -= amount
        else:
            print("invalid Pin")

    def balance(self, balance, pin):
        if self.pin == pin:
            return self.balance()
        else:
            print("Invalid Pin")

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
