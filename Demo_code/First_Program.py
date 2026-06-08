# Print Hello World
print("Hello World")

# Create a variable to store my name
first_name = "Katherine"

# Create a variable for the last name
last_name = "Levings"

# Write a python statement to display "My fullname is Firstname Lastname"
print("My full name is", first_name, last_name, sep="---")

# print using the f string (String Interpolation)
print(f"My full name is {first_name} {last_name}.")

# Create variables to store my age and weight
age = 16
weight = 148.3
half_age = age / 2

# print a sentence with name, weight, and age
print(f"My name is {first_name} {last_name}.\nI am {age} years old and I weigh {weight} pounds. Half of my age is {half_age}.")

# get and print the data type for age, weight, and half_age
print("\nChecking data types for age, weight, and half_age:\n------------")
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 statements using string interpolation to print descriptive sentences for the data types.
print(f"Variable age is a {type(age)}.")
print(f"Variable weight is a {type(weight)}.")
print(f"Variable half_age is a {type(half_age)}.")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")