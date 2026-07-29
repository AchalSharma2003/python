# start to end print even numbers

start = int(input("enter the starting point : "))
end = int(input("enter the ending point : "))

i = start
n = end

while i<=n:
    if i%2 == 0:
        print(i)
    i+=1