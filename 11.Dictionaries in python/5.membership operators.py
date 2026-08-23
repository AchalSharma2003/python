student = {
    'name': 'achal', 
    'age': 22, 
    'gender': 'male', 
    'city': 'delhi', 
    'phone': 7934875683, 
    'state': 'MP'
}

# print("age" in student)
# print(35 in student)

k = input("enter the key: ")

if k in student:
    print(student[k])
else:
    print("key does not exist")