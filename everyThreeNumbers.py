#Write your function here
def every_three_nums(start):
  result = []
  while start <=100:
    result.append(start)
    start+=3
  
  return result

#Uncomment the line below when your function is done
print(every_three_nums(91))