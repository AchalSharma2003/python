student = {"name": "achal", "age": 22}

# update
student["age"] = 23
print(student)

# add
student["gender"] = "male"
print(student, id(student))

student.update(
    {
        "city": "delhi",
        "phone" : 7934875683,
        "state" :"MP",
        "age" : 22
    }
)

print(student, id(student))