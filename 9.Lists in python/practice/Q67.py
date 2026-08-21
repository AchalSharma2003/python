"""
Given a list of marks, use list comprehension to create a new list that 
contains only the marks that are above 75.
"""

marks = [65, 80, 70, 90, 75, 82, 60]

marks_g = [num for num in marks if num>=75]
print(marks_g)