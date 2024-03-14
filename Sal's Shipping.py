weight = 8.4

#Ground Shipping
if weight <= 2.0:
  cost = (weight * 1.5) + 20
elif weight <= 6.0:
  cost = (weight * 3) + 20
elif weight <= 10:
  cost = (weight * 4) + 20
elif weight >= 20:
  cost = (weight * 4.75) +20
else:
  cost = weight

print("$",cost)

#Ground Shipping Premium
premimum = 125
print("$", premimum)

weight = 1.5
#Drone Shipping Premium
if weight <= 2.0:
  cost = weight * 4.5
elif weight <= 6.0:
  cost = weight * 9
elif weight <= 10:
  cost = weight * 12
elif weight >= 20:
  cost = weight * 14.25
else:
  cost = weight

print("$", cost)