# Create a function that returns True if num is in greater than lower and less than greater else return False

def in_range(num, lower, upper):
  if (num >= lower and num <= upper):
    return True
  else:
    return False

print(in_range(10, 10, 10))
print("")
print(in_range(5, 10, 20))