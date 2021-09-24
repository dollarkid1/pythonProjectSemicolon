import datetime
import math


class Loan:
    def __init__(self, annual_interest_rate, number_of_years, loan_amount):
        self.annual_interest_rate = annual_interest_rate
        self.number_of_years = number_of_years
        self.loan_amount = loan_amount
        self.date = datetime.datetime.now()

    def get_annual_interest(self):
        return self.annual_interest_rate

    def set_annual_interest(self, annual_interest_rate):
        self.annual_interest_rate = annual_interest_rate

    def get_numbers_of_years(self):
        return self.number_of_years

    def set_numbers_of_years(self, number_of_years):
        self.number_of_years = number_of_years

    def get_loan_amount(self):
        return self.loan_amount

    def set_loan_amount(self, loan_amount):
        self.loan_amount = loan_amount

    def get_monthly_payment(self):
        monthly_interest_rate = self.annual_interest_rate / 1200
        monthly_payment = self.loan_amount * monthly_interest_rate
        (1 - (1 / math.pow(1 + monthly_interest_rate, self.number_of_years * 12)))
        return monthly_payment

    def get_total_payment(self):
        total_payment = self.get_monthly_payment() * self.number_of_years * 12
        return total_payment

    def get_date(self):
        return self.date


if __name__ == '__main__':
    annual_interest_rate = float(input("Enter annual interest rate, for example, 8.25: "))
    number_of_years = int(input("Enter number of years as an integer: "))
    loan_amount = float(input("Enter loan amount, for example, 120000.95: "))

    loan = Loan(annual_interest_rate, number_of_years, loan_amount)

    print(f'The loan was created on {loan.get_date()}\n'
          f'The monthly payment is {loan.get_monthly_payment()}\n'
          f'{loan.get_total_payment()}')
