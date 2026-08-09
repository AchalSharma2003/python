"""
Write a function called find_max that takes three numbers as 
parameters and prints the largest one.
"""

def find_max(a,b,c):
    if a>b and a>c:
        print(f"{a} is the max out of three")
    elif b>a and b>c:
        print(f"{b} is the max out of three")
    else:
        print(f"{c} is the max out of three")

find_max(10,20,30) 