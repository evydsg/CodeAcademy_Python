def append_sum(my_list):
  index = 0
  sum = 0
  while index !=3:
    sum = my_list[len(my_list)-1] + my_list[len(my_list)-2]
    my_list.append(sum)
    index+=1
  
  return my_list


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
