"""
Q12: Take three numbers as input. Print the largest of the three without using any 
built-in function.
"""

a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))

if a>b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")