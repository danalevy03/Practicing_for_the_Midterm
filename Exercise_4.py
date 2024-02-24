#  Write a function that takes the name of a text file as parameter.
#  Print out the 3-letter words that start with “b”

def print_3_letter_words_starting_with_b(file_name):
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                if len(word) == 3 and word[0] == "b":
                    print(word)

print_3_letter_words_starting_with_b("text.txt")

