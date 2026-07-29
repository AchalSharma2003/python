# start to end,print from start to end

start = int(input("enter the number : "))
end = int(input("enter the number : "))
total = 0
for i in range(start,end+1):
    total+=i
    print(i)

print(f"total is {total}")