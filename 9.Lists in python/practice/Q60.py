"""
Given two lists, merge them into a single new list without modifying the 
originals.
"""

# def merge_two_lst(lst1, lst2):
#     return lst1 + lst2

def merge_two_lst(lst1, lst2):
    new_lst = []
    for num in lst1:
        new_lst.append(num)
    for num in lst2:
        new_lst.append(num)
    return new_lst

num1 = [1, 2, 3]
num2 = [65, 32, 11]
print(merge_two_lst(num1,num2))