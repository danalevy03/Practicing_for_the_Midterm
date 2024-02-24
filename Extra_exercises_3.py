#Write a function that takes a list of numbers as a parameter and returns a new list containing only the odd numbers squared.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd_numbers_squared(numbers):
    while True:
        try:
            odd_numbers = [x ** 2 for x in numbers if x % 2 != 0]
            return odd_numbers
        except ValueError:
            print("Invalid input")

print(odd_numbers_squared(numbers))

#OR
def square_odd_numbers(input_list):
    return [x**2 for x in input_list if x % 2 != 0]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_odd_numbers(numbers)
print(result)

#Write a function that takes the name of a text file as a parameter. Read the contents of the file and print the average length of words.
# Handle potential file not found or reading errors using try/except.

def average_word_length(file_name):
    try:
        with open(file_name, "r") as file:
            words = file.read().split()
            if not words:
                return 0
            average = sum(len(word) for word in words) / len(words)
            return average
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(e)
        return None

print(average_word_length("text.txt"))

#Write a recursive function that calculates the factorial of a given number.

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

print(factorial(5))

#Write a function that generates and returns a list of 5 random numbers between 1 and 100.

import random

def random_numbers():
    return [random.randint(1, 100) for _ in range(5)]

print(random_numbers())



