"""3: Take the user's age as input. Check and print whether they are eligible 
to vote (age >= 18) and whether they are a senior citizen (age >= 60). 
Print both results."""

age = int(input("enter your age : "))

can_vote = age>=18
is_senior_citizen = age>=60

print(f"eligible to vote : {can_vote}")
print(f"senior citizen :{is_senior_citizen}")