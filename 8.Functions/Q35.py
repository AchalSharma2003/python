"""
Write a function that ask a number from user and prints if that 
number is odd or even.
"""

def oddeven():
    num = int(input("enter the number : "))
    if num%2 == 0:
        print("even")
    else:
        print("odd")

oddeven()