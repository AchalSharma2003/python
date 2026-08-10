"""
Create a list of 5 of your favourite movies. Print the first, last,
 and middle movie from your list using both positive and negative 
 indexing where appropriate
"""


movies = ["kgf","avengers","iron man","stranger things","mirzapur"]
n = len(movies)
print(f"first movie is : {movies[0]}")
print(f"first movie is : {movies[n//2]}")
print(f"first movie is : {movies[-1]}")