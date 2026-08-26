marks = {
    "science" : 98,
    "maths" : 99,
    "computer" : 100,
    "web dev" : 100,
    "analytics" : 89
}

print(marks.keys())
for sub in marks.keys():
    print(sub)

total = 0
for sub in marks.keys():
    print(f"subject = {sub} , marks = {marks[sub]}")
    total += marks[sub]
print(total)