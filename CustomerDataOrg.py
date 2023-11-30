first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

expedited_shipping = [True, False, True, False]

customer_data = [
    [first_names[0], preferred_size[0], expedited_shipping[0]],
    [first_names[1], preferred_size[1], expedited_shipping[1]],
    [first_names[2], preferred_size[2], expedited_shipping[2]],
    [first_names[3], preferred_size[3], expedited_shipping[3]]
]

print(customer_data)

customer_data[2][2] = False
customer_data[1].remove(False)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)