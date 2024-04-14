sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for locations in location:
    scoops_sold+= locations

print(scoops_sold)