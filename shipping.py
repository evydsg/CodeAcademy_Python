weight = 8.4

#Ground Shipping
flat_charge = 20
if weight <=2:
  price_pound = 1.5
  print(weight * price_pound + flat_charge)
elif weight > 2 and weight <= 6:
  price_pound = 3
  print(weight * price_pound + flat_charge)
elif weight > 6 and weight <=10:
  price_pound = 4
  print(weight * price_pound + flat_charge)
elif weight > 10:
  price_pound = 4.75
  print(weight * price_pound + flat_charge)

#Drone Shipping
weight_drone = 1.5
if weight_drone <=2:
  price_pound = 4.5
  print(weight_drone* price_pound)
elif weight_drone > 2 and weight_drone <= 6:
  price_pound = 9
  print(weight_drone * price_pound)
elif weight_drone > 6 and weight_drone <=10:
  price_pound = 12.00
  print(weight_premium * price_pound)
elif weight_drone > 10:
  price_pound = 14.25
  print(weight_drone * price_pound)