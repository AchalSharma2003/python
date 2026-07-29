# Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100.

i = 1
n = 100

while i<=n:
    if i%3 == 0 and i%5 == 0:
        print(i)
    i+=1