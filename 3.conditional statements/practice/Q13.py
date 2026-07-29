"""
Q13: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line
"""

a = int(input("enter the number : "))

finder = "even" if a%2 == 0 else "odd"

print(f"{a} is {finder}")