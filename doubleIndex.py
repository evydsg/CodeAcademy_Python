def double_index(my_list, index):
  new_list = []

  if index >= len(my_list):
    return my_list
  for ind in range(len(my_list)):

    if my_list[ind] == my_list[index]:
      new_list.append(my_list[ind]*2)
    else:
      new_list.append(my_list[ind])
    
  return new_list



#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))