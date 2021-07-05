annualInterestRate = eval(input("Enter annual interest rate e.g 7.5:"))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("Enter numbers of Years, e.g 5"))
loanAmount = eval(input("Enter Loan amount, e.g 12300.99"))

monthlyPayment = loanAmount * annualInterestRate / \
                 (1 - 1 / (1 + monthlyInterestRate) **
                  (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) / 100)
