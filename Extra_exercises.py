# Create variables for a person's name, age, and city.
# Use string formatting to print a sentence like "John is 25 years old and lives in Segovia."

name = "John"
age = 25
city = "Segovia"

print(f"{name} is {age} years old and lives in {city}.")

# Write a program that takes a year as input and prints whether it's a leap year or not.

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Create a list of words. Write a loop to print each word in uppercase.
words = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words:
    print(word.upper())

#Write a function calculate_triangle_area that takes the base and height of a triangle as parameters and returns the area.
#Test the function with different values.

def calculate_triangle_area(base, height):
    return 0.5 * base * height

print(calculate_triangle_area(3, 4))
print(calculate_triangle_area(5, 6))
print(calculate_triangle_area(7, 8))


#Create a program that reads a text file containing a list of numbers, each on a new line.
# The program should calculate the sum of these numbers and print the result.

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)

#Generate a list of squares of numbers from 1 to 10 using a list comprehension.
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# Create a string with mixed uppercase and lowercase characters.
# Write a program to count and print the number of uppercase and lowercase letters.

string = "HeLLo WoRlD"
upper = 0
lower = 0
for char in string:
    if char.isupper():
        upper += 1 # upper = upper + 1
    elif char.islower():
        lower += 1 # lower = lower + 1

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

#Write a program to print a multiplication table (up to 10) using nested loops.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

