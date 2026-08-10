marks = [11,32,54,23,55,54,67,89]

# to get the length
n = len(marks)
print(f"length of marks : {n}")

# max
maxi = max(marks)
print(f"maximum of marks : {maxi}")

# min
mini = min(marks)
print(f"minimum of marks : {mini}")

# total
total = sum(marks)
print(f"total of marks : {total}")

# to sort using sorted(),it will always return you a new list
new_marks = sorted(marks)
new_marks1 = sorted(marks, reverse = True)
print(new_marks)
print(new_marks1)