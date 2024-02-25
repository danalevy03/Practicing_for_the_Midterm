# Write a recursive function to calculate the sum of all positive integers from 1 to a given number n.

def sum_positive_integers(n):
    if n == 1:
        return 1
    return n + sum_positive_integers(n - 1)

print(sum_positive_integers(5))
print(sum_positive_integers(10))
print(sum_positive_integers(15))

# Write a function that takes a string as input and returns the string in reverse order.
def reverse_string(string):
    return string[::-1]

print(reverse_string("Hello World"))
print(reverse_string("Python Programming"))

#Create a list of numbers.
# Write a program to find and print the maximum and minimum values in the list.
numbers = [3, 5, 1, 7, 9, 2, 8, 4, 6]
print(max(numbers))
print(min(numbers))

#Create a class Circle with methods to calculate its area and circumference.
# Create an instance and test the methods.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(6)

print(circle.area())
print(circle.circumference())

#Write a program to print the Fibonacci series up to 10 terms.
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

#Write a program that reads an integer from the user. Handle exceptions for invalid inputs (non-integer) and prompt the user until a valid input is provided.
while True:
    try:
        number = int(input("Enter a number: "))
        number = 10/ number
        break
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")

#Write a program to print the first 10 square numbers.
for i in range(1, 11):
    print(i ** 2, end=" ")
print()

#Create a list of words. Write a program to sort the list alphabetically.
words = ["apple", "cherry", "banana", "elderberry", "juice"]
words.sort()
print(words)

#Write a function that takes a list of numbers as input and returns a new list with only the even numbers.
def even_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Write a program that prompts the user to enter two numbers and prints their sum, difference, product, and quotient.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result1 = number1 + number2
result2 = number1 - number2
result3 = number1 * number2
result4 = number1 / number2

print(f"Sum: {result1}")
print(f"Difference: {result2}")
print(f"Product: {result3}")
print(f"Quotient: {result4}")

