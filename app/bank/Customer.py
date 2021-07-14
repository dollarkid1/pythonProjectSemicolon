class Customer:
    def __init__(self, first_name, last_name, date_of_birth, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number
