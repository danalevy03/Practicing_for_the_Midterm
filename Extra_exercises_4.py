# Write a function that takes a sentence as input and returns a new sentence with each word reversed.
# Maintain the order of words in the sentence.

def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

print(reverse_words("Hello World"))

# Write a one-liner using list comprehension to create a list of prime numbers between 1 and 50.
primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, x))]
print(primes)

# Write a program that takes a user's age as input. If the age is less than 18, print "You are a minor."
# If the age is between 18 and 65, print "You are an adult."
# Otherwise, print "You are a senior citizen."

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Create a nested list representing a matrix.
# Write a program to find the determinant of a 3x3 matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
determinant = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
print(determinant)

#Write a program that reads a text file containing a list of words.
#Print the top three most frequent words along with their frequencies.

from collections import Counter

with open("words.txt", "r") as file:
    words = file.read().split()
    word_count = Counter(words)
    print(word_count.most_common(3))

#Write a function that takes a mathematical expression as input (e.g., "2 + 3 * 4") and evaluates it.
# Handle potential syntax errors using try/except.

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except SyntaxError:
        print("Invalid syntax")
        return None
    except Exception as e:
        print(e)
        return None

print(evaluate_expression("2 + 3 * 4"))

#Write a program to print a pattern of numbers in the shape of a pyramid.

def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for k in range(i, 0, -1):
            print(j, end="")
        for l in range(2, i + 1):
            print(l, end="")
        print()

print_pyramid(5)

# Create two sets of strings.
# Write a program to print the common substrings of length 3 or more in both sets.

set1 = {"apple", "banana", "cherry", "date", "elderberry"}
set2 = {"banana", "date", "elderberry", "fig", "grape"}
common_substrings = {word[i:i+3] for word in set1 for i in range(len(word)-2) if word[i:i+3] in {word2[j:j+3] for word2 in set2 for j in range(len(word2)-2)}}
print(common_substrings)

#Write a program that takes a list of sentences as input and prints them sorted by the number of words in each sentence.

sentences = ["This is a sentence made by Dana.", "This is another sentence.", "This is a third sentence."]
sorted_sentences = sorted(sentences, key=lambda x: len(x.split()))
print(sorted_sentences)

# hola












