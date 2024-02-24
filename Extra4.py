#Write a program that takes user input for a number.
# Use try/except blocks to handle exceptions if the input is not a valid number.

# number = input("Enter a number: ")
# try:
   # number = int(number)
  #  print(f"The number is {number}")
# except ValueError:
  #  print("Invalid input")


# Modify the program to handle the ValueError and ZeroDivisionError exceptions separately.

number = input("Enter a number: ")
try:
    number = int(number)
    number = 10 / number
    print(f"The number is {number}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")





