# python offers methods like
# remove(),discard(),pop() and clear() to manage set elements

python_fruits = {'banana', 'pineapple', 'apple', 'mango', 'papaya', 'kiwi'}
# python_fruits.remove("apple")
# python_fruits.discard("apple")
# python_fruits.clear()
remove = python_fruits.pop()

print(f"removed element = {remove}")

print(python_fruits)