loan_amount = 1000
loan_intrest_rate = 5
loan_term = 10

for i in range(loan_term):
  loan_amount = loan_amount + (loan_amount * loan_intrest_rate /100)
print(loan_amount)
