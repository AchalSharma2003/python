marks = {
    "science" : 98,
    "maths" : 99,
    "computer" : 100,
    "web dev" : 100,
    "analytics" : 89
}

print(marks.items())
# for details in marks.items():
#     sub = details[0]
#     mark = details[1]
#     print(sub,mark)

# for k,v in marks.items():
#     print(k,v)

for sub,mark in marks.items():
    print(sub,mark)

