def more_frequent_item(my_list, item1, item2):
  count1 = my_list.count(item1)
  count2 = my_list.count(item2)

  if count1> count2:
    return item1
  elif count1< count2:
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))