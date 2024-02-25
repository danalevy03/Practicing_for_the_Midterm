
# Use an f-string to print a message with the current year.
from datetime import datetime

current_year = datetime.now().year
print(f"The current year is {current_year}.")

#Write a program that opens a file, writes a message, and closes the file.
with open("message.txt", "w") as file:
    file.write("Hello, World!")

closed = file.closed
print(closed)

#Write a function that prints a welcome message. Call the function.
def welcome_message():
    print("Welcome!")

welcome_message()

#Write a function that takes two numbers as parameters and returns their sum.

def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 3))

#Create a list of fruits. Print each fruit on a new line using a for loop.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

#Concatenate two lists and print the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2 # concatenation
print(result)

#Use the append method to add an element to a list.
list1.append(4)
print(list1)

#Remove an element from the list and print the updated list.
list1.remove(4)
print(list1)





