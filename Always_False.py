# Create a function is retruns False no matter the number

def always_false(num):
  if num < 0 and num > 0:
    return True
  else:
    return False


print(always_false(0))
print("")
print(always_false(-1))
print("")
print(always_false(1))
