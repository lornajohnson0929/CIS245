initial_investment = float(input("Please enter the initial investment. Note please enter the initial investment as a whole number:"))
rate = int(input("Please enter the interest rate. Note please enter the rate as a whole number:"))

year = 0
total = initial_investment

while total <= initial_investment*2:

    total = total+total*(rate)/100
    year = year+1


print("Years to double investment is",year)
