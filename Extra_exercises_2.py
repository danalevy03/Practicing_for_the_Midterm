#Write a function that takes the name of a text file as a parameter.
# Print out all the words that are palindromes in the file.

def print_palindromes(file_name):
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                if word == word[::-1]:
                    print(word)

print_palindromes("text.txt")

#Write a function that takes an integer as a parameter and returns a list of all the prime divisors of that number.

def prime_divisors_of_number(number):
    prime_divisors = []
    for i in range(2, number+1):
        if number % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_divisors.append(i)
    return prime_divisors

print(prime_divisors_of_number(900))

# Write a function that forces the user to enter an even number.
#Use try/except to catch invalid inputs. Return that even number.

def even_number():
    while True:
        try:
            number = int(input("Enter an even number: "))
            if number % 2 == 0:
                return number
            else:
                print("This is not an even number")
        except ValueError:
            print("Invalid input")

print(even_number())

#Write a function that takes a string as a parameter and returns a new string with all vowels replaced by asterisks (*).

def replace_vowels(string):
    vowels = "aeiou"
    new_string = ""
    for char in string:
        if char.lower() in vowels:
            new_string += "*"
        else:
            new_string += char
    return new_string

print(replace_vowels("Hello World"))

# Write a function that takes two lists as parameters and returns a new list containing the common elements between the two lists.
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(common_elements(["apple", "banana", "cherry"], ["banana", "date", "elderberry"]))

# Write a function that prompts the user to enter a number between 1 and 10 (inclusive). Use try/except to catch invalid inputs. Return the valid input.
def number_between_1_and_10():
    while True:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if 1 <= number <= 10:
                return number
            else:
                print("This is not a valid number")
        except ValueError:
            print("Invalid input")

print(number_between_1_and_10())















