#Write a program that takes two numbers as input and prints their remainder when divided.

def remainder():
    while True:
        try:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            return number1 % number2
        except ValueError:
            print("Invalid input")

print(remainder())

#Create a boolean variable is_sunny and print "Go outside!" if it's True and "Stay inside." if it's False.

is_sunny = False
print("Go outside!" if is_sunny else "Stay inside.")

#Declare a variable for your age and print a message using an f-string.

age = 20
print(f"I am {age} years old.")

#Write a program that takes a user's name as input and prints a personalized greeting. no numbers allowed.

while True:
    name = input("Enter your name: ")
    if name.isalpha():
        print(f"Hello, {name}!")
        break
    else:
        print("Invalid input")

#Write a program that prompts the user to enter a number.
# Handle the ValueError if a non-numeric value is entered.

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input")

#Write a program that checks if a given number is positive, negative, or zero.

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Write a program that prints numbers from 1 to 5 using a while loop.

i = 1
while i <= 5:
    print(i)
    i += 1

#Write a program with an infinite loop that prints "Hello" repeatedly.
# Terminate the program manually.

# while True:
   # print("Hello")

#Write a program that prints the squares of numbers from 1 to 5 using a for loop.

for i in range(1, 6):
    print(i ** 2)

#Create two strings and concatenate them. Print the result.

string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)

#Use the format operator to print a message with a placeholder for a variable.

name = "Alice"
print("Hello, %s!" % name) # %s is a placeholder for a string


