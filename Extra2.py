#Write a program that takes an integer as input. Print whether it's positive, negative, or zero.

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Write a loop to print the first 10 even numbers.

for i in range(2, 21, 2):
    print(i)

#Create a list my_list with at least five numbers. Append a new number, print a slice of the list, and print its length.

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list[:3])
print(len(my_list))

#Write a function calculate_factorial that takes an integer as input and returns its factorial. Test the function with a number of your choice.
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return factorial

print(calculate_factorial(5))


