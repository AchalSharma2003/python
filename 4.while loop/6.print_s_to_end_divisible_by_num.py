# print start to end,numbers which are divisible by 3 and 4

start = int(input("enter the starting point : "))
end = int(input("enter the ending point : "))

i = start
n = end

while i<=n:
    if i%3 == 0 and i%4 == 0:
        print(i)
    i+=1