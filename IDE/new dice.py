# Task 1: Analyze and count the variables in the program
company = "ABC Data"  # String type
phone = "555-123-009"  # String type
employees = 25  # Integer type
remote_work = True  # Boolean type
big_company = employees > 100  # Boolean type (True or False)
income = 4500000  # Integer type
income_per_person = income / employees  # Float type

# Count of variables: 7
# Variables and their properties:
# 1. company = "ABC Data" -> String
# 2. phone = "555-123-009" -> String
# 3. employees = 25 -> Integer
# 4. remote_work = True -> Boolean
# 5. big_company = employees > 100 -> Boolean
# 6. income = 4500000 -> Integer
# 7. income_per_person = 4500000 / 25 -> Float

# Task 2: Modify the program to calculate the sum of three numbers
number1 = 71
number2 = 14
number3 = 23  # New third number
result = number1 + number2 + number3  # Sum of three numbers

# Printing the results
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

# Task 3: Swap two variable values using an auxiliary variable
x = 7
y = 34
z = 0  # auxiliary variable

print("Before swapping: x=", x, "y=", y)

# Swapping values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)

# Task 4: Convert speed from km/h to m/s
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600  # Conversion formula
print(speed_kmh, "km/h = ", speed_ms, "m/s")

# Task 5: Calculate the diagonal length of a rectangle
import math

a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)  # Using Pythagorean theorem

print("Length of the diagonal: ", diagonal)

# Task 6: Calculate the distance to the horizon based on height
height = float(input("Enter the height of the observer in meters: "))
distance = 3.57 * math.sqrt(height)

print(f"The distance to the horizon is {distance:.2f} kilometers.")

# Task 7: Calculate the world population and distribution between hemispheres
total = 8000000000  # World population
north = 7200000000  # Population in the Northern Hemisphere
south = total - north  # Population in the Southern Hemisphere

print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", (north / total) * 100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", (south / total) * 100)

# Task 8: Fix the program that calculates the average grade of a student
math = 5
art = 4
music = 5
history = 3  # Fixing history grade to integer

average = (math + art + music + history) / 4  # Corrected formula

print(f"Average grade is {average}")

# Task 9: Print student data using f-strings
name = "Adam"
age = 20
height_cm = 180

# Printing student data
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height_cm} cm.")
print(f"In 6 years I will be {age + 6} years old.")

# Task 10: Family income per person using f-strings
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members

print(f"Total family income is {total_income}, and income per person is {income_per_person:.2f}")

# Task 11: Print arithmetic expressions between variables a and b
a = 3
b = 5

print(f'{a}+{b}={a + b}')
print(f'{a}-{b}={a - b}')
print(f'{a}*{b}={a * b}')
print(f'{a}/{b}={a / b}')

# Program collects user input for several small tasks:
# - read first/last name and print full name
# - cube volume & surface area
# - cuboid volume & surface area
# - compute 23% VAT for an amount
# - compute price after discount

# 1) Read and print full name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Your first name is {first_name} and your last name is {last_name}")
print(f"And your full name is {full_name}")

print()  # separator

# 2) Cube: volume and surface area
cube_side_string = input("Enter cube side: ")
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = 6 * cube_side ** 2
print(f"The volume of a cube with side {cube_side} is {cube_volume}")
print(f"The surface area of a cube with side {cube_side} is {cube_surface_area}")

print()  # separator

# 3) Cuboid: read a, b, c and compute volume & surface area
a = int(input('Enter the length (a): '))
b = int(input('Enter the width (b): '))
c = int(input('Enter the height (c): '))

# Volume of the cuboid is length * width * height
cuboid_volume = a * b * c

# Surface area of the cuboid is 2*(ab + ac + bc)
cuboid_surface_area = 2 * (a * b + a * c + b * c)

# Print the results
print(f'The volume of the cuboid with sides a={a}, b={b}, c={c} is {cuboid_volume}')
print(f'The surface area of the cuboid with sides a={a}, b={b}, c={c} is {cuboid_surface_area}')

print()  # separator

# 4) VAT 23% calculation
amount = float(input("Enter amount: "))
vat = amount * 0.23
print(f"Amount  : {amount:.2f}")
print(f"VAT 23% : {vat:.2f}")

print()  # separator

# 5) Price and discount
price = float(input("Enter price: "))
discount_percent = float(input("Enter discount %: "))
discounted_price = price * (1 - discount_percent / 100)
reduction = price - discounted_price
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")

# A program that calculates the number of characters
# of your name, surname and full name

name = 'Marek'    
surname = 'Zmelty' 
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name + " " + surname)} characters')

# A program that prints your initials

name = 'George'
surname = 'Smith'

# Print initials
print(name[0] + surname[0])

# A program that prints a university abbreviation

university = "Krakow University of Economics"
abbreviation = "".join([word[0] for word in university.split()])
print(abbreviation)  # Output will be "KUE"

# A program for printing detailed information.

employee = "Mr. John May, born on 1998-02-16"
name = employee[4:8]
surname = employee[9:13]
dob = employee[-10:]
initials = name[0] + surname[0]

print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {dob}')
print(f'Initials: {initials}')

# A program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.

phone = input('Enter phone number: ')
formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
print(f'Phone number: {formatted_phone}')

# A program to print numerical representations of characters.

print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')

# A program that prints a numerical representation of each letter of your name.

name = 'Marek'  
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')

# A program that calculates
# how many letters are between two given letters

first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)

# Calculate how many letters are between
number_of_letters = abs(last_letter_code - first_letter_code) - 1

print(f'Between {first} and {last} is {number_of_letters} letters')

# Character code conversion

print(chr(67), chr(111), chr(111), chr(108), chr(33))  # Output: C o o l !

# String manipulation

movie = "The Lord of the Rings: The Return of the King"

# Print number of characters
print('Number of characters: ', len(movie))

# Print title in capital letters
print(movie.upper())

# Print title in small letters
print(movie.lower())

# Print how many times the vowel "e" appears in the title
print('Number of times "e" appears: ', movie.count('e'))

# Print where in the text is the word "Lord"
print('The word "Lord" starts at index: ', movie.find('Lord'))

# Print where in the text is the word "dragon"
print('The word "dragon" starts at index: ', movie.find('dragon'))

