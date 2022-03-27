# Create a function that will return a very brief non-descriptive review of the movie in question

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  elif rating >= 9:
    return "Outstanding!"
  else:
    return (print("Error"))


print(movie_review(9))
print("")
print(movie_review(4))
print("")
print(movie_review(6))