"""Q4: A student scored marks in 3 subjects. Take all three as input, 
calculate the total and average, and print both using an f-string."""

maths = int(input("enter the marks :"))
science = int(input("enter the marks :"))
english = int(input("enter the marks :"))

total = maths + science + english
print(f"total:{total}")
average = total/3
print(f"average:{average}")
