hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for i in range(len(prices)):
  total_price+=prices[i]

average_price = total_price/len(prices)
print(average_price)

new_prices = [price-5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = prices[i]+last_week[i]

print(f"Total Revenue: ${total_revenue:.2f}")
average_daily_revenue = total_revenue/7

cuts_under_30 = [price for price in new_prices if price < 30]
print(cuts_under_30)