"""
Write a program that takes a list and a target number. 
Use a loop to determine if the target number exists in the list.
 Do not use the in operator.
"""


nums = [6, -5, 4, 2, 10, 91, 75, 49, 9]


def is_target(lst,target):
    for num in lst:
        if num == target:
            return True
    return False

print(is_target(nums,10))