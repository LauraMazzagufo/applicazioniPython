#A common thing people do is borrow money. When people repay money, they pay interest
#which is paid back annually and added to the original amount the person borrowed.
#You are going to create a loan calculator that shows how much money you owe
#for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.
#This means each year the amount of money you owe will increase 5%.
#Figure out how much you owe altogether for 10 years?
#Use a for loop and one or two lines of looped code to determine the answer.
#(Hint: Don't make this overcomplicated. It should only be a few lines of code altogether.)

print("LOAN CALCULATOR")

loan = int(input("Type the amount of money you borrowed: loan = "))
percentual_apr = float(input("Type the Annual Percentage Rate: APR = "))
print()
apr = percentual_apr/100
for i in range (10):
  loan += (loan*apr)
  print("After", i+1, "year(s), your loan is $", round(loan, 2))
