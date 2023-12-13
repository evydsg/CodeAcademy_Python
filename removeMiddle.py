def remove_middle(my_list, start, end):
  first_list = my_list[:start]
  second_list = my_list[end+1:]
  third_list = first_list + second_list
  return third_list
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))