def in_range(num1, num2, num3):
  if num1 >= num2 and num1 <= num3:
    return True
  else:
    return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False