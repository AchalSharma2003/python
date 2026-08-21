# 1 to 20, but only even numbers

# new_lst = [i for i in range(1, 21) if i%2 == 0]
# new_lst = [i for i in  range(1, 101) if i%3 == 0 or i%8 == 0]
# print(new_lst)

# from 1 to 100 make the list of all prime numbers

def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num%i == 0:
            factors += 1
    if factors == 2:
        return True
    return False

new_lst = [i for i in range(2, 101) if is_prime(i) == True]
print(new_lst)