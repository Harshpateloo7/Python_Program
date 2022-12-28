#In this exercise, you'll create a list and then answer questions about that list.
#a.
#Create a list of temperatures in degrees Celsius with the values 25.2,
#16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign it to a variable called
#temps.
#b.
#Using one of the list methods, sort temps in ascending order.
#C.
#Using slicing, create two new lists, cool temps and warm temps, which contain
#the temperatures below and above 20 degrees Celsius, respectively.
#d
#Using list arithmetic, recombine cool temps and warm temps into a new
#list called temps in celsius.


temps = [25.2,16.8,31.4,23.9,28,22.5,19.6]

temps.sort()

print(temps)

cool_temps = temps[:2]
print(cool_temps)
warm_temps = temps[2:]
print(warm_temps)
temps_in_celsius =[cool_temps + warm_temps]

print(temps_in_celsius)