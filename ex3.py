#number of cars
cars = 100
#space in car exluding the driver
space_in_a_car = 4 #nothing seems to happen...
#number of people who can drive
drivers = 30
#number of people who cant drive
passengers = 90
#quik mafs
cars_not_driven = cars - drivers
#logic
cars_driven = drivers
#more mafs
carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven #the 's' in passengers was missing

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, " poeple in each car.")
