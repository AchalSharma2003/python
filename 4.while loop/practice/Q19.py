# Q19. Ask a number from the user, and print all the factors.

# num = int(input(" enter the number : "))
# i = 1
# while i<=num:
#     if num%i == 0:
#         print(i)
#     i+=1


    # Q19. Ask a number from the user, and count all the factors.

num = int(input(" enter the number : "))
i = 1
count = 0
while i<=num:
    if num%i == 0:
        count+=1
    i+=1
print(f"total number of factors are {count}")
