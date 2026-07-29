# Q18. Ask a number from the user, print the multiplication table upto 10.

i = int(input("enter the number : "))
n = 1

while n<=10:
    print(f"{i} *{n} = {i*n}")
    n+=1
    