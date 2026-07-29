"""Q8: Take two numbers as input. Print the greater of the two. If they are 
equal, print "Both are equal."""

a = int(input("enter the number : "))
b = int(input("enter the number : "))

if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print("both are equal")
else:
    print(f"{b} is sgreater than {a}")