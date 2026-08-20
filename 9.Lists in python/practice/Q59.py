"""
Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

def reverse_lst(lst):
    n = len(lst)
    new_lst = []
    for i in range(n - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

nums = [1, 2, 54, 85, 23, 3, 8, 2]

ans = reverse_lst(nums)
print(ans)