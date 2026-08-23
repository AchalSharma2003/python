marks = {
    "science":99,
    "maths":98,
    "english":99,
    "computer":96,
    1:10
}
# print(marks["science"])
# print(marks.get("science"))
# print(marks.get("sciencee", 0))

subject = "computer"

ans = marks.get(subject)
if ans is None:
    print("subject not found")
else:
    print(f"marks scoe of subject = {ans}")