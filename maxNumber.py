def max_num(nums):
  max_value = nums[0]

  for num in nums:
    if num > max_value:
      max_value = num
    
  return max_value

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))