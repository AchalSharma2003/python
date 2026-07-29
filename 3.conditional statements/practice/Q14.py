"""
Q14: A shop gives discounts based on purchase amount:
Above 5000 →20% discount
Above 2000 →10% discount
Above 1000 →5% discount
1000 or below →no discount
"""

spent_amount = int(input("enter the amount that is spent : "))

if spent_amount>5000:
    print(f"the discount you got is 20% which is {spent_amount*0.2}")
elif spent_amount>2000 and spent_amount<=5000:
    print(f"the discount you got is 10% which is {spent_amount*0.1}")
elif spent_amount>1000 and spent_amount<=2000:
    print(f"the discount you got is 5% which is {spent_amount*0.05}")
else:
    print("no discount")

