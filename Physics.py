train_mass = 22680
train_acceleration = 10
C = 3*10**8
train_distance = 100
bomb_mass = 1

# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp*9/5+32
  return f_temp

def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass, c):
  return mass * c**2

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

f_100_in_celsius = f_to_c(100)
print(f_100_in_celsius)

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

train_force = get_force(train_mass, train_acceleration)

print(f"The GE train supplies {train_force} Netwons of force")

bomb_energy = get_energy(bomb_mass, C)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over Y meters.")