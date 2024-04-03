# Your code below:
toppings = [
"pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"
]

prices =[
2,
6,
1,
3,
2,
7,
2
]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = []
for num in range(len(toppings)):
    pizza_and_prices += [[prices[num], toppings[num]]]

print(pizza_and_prices)

pizza_and_prices.sort()

print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

pricest_pizza = pizza_and_prices.pop()

pizza_and_prices += [2.5, "peppers"]

three_cheapest = pizza_and_prices[:3]
print("\n",three_cheapest)
