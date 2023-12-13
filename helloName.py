def add_greetings(names):
  greetings = []
  for name in names:
    greeting = "Hello, "+ name
    greetings.append(greeting)
  
  return greetings


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))