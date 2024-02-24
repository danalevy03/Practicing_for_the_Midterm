#Declare variables my_integer, my_float, my_string, and my_boolean.
#Print their values and types.

my_integer = 5
my_float = 5.0
my_string = "5"
my_boolean = True

print(my_integer, type(my_integer))
print(my_float, type(my_float))
print(my_string, type(my_string))
print(my_boolean, type(my_boolean))

#Prompt the user to input two numbers.
#Perform addition, subtraction, multiplication, division, and modulus operations and print the results.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print(f"Addition: {number1 + number2}")
print(f"Subtraction: {number1 - number2}")
print(f"Multiplication: {number1 * number2}")
print(f"Division: {number1 / number2}")
print(f"Modulus: {number1 % number2}")

# Create a string my_string with any content.
# Print the string, its length, and a slice that includes the first three characters.

my_string = "Hello, World!"
print(my_string)
print(len(my_string))
print(my_string[:3])




