marks = {
    "science" : 98,
    "maths" : 99,
    "computer" : 100,
    "web dev" : 100,
    "analytics" : 89
}

total = 0
for mark in marks.values():
    print(mark)
    total += mark
print(f"total = {total}")