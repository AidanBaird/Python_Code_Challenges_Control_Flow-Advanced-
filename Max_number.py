# Create a function that will return the highest number put into the function or return "It's a tie" otherwise

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"


print(max_num(-10, 0, 10))
print("")
print(max_num(-10, 5, -30))
print("")
print(max_num(-5, -10, -10))
print("")
print(max_num(2, 3, 3))