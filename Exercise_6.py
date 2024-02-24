# Write a function that forces the user to enter a multiple of 6 number.
# Use try,except to catch invalid inputs. Return that number

def multiple_of_6():
    while True:
        try:
            number = int(input("Enter a multiple of 6: "))
            if number % 6 == 0:
                return number
            else:
                print("This is not a multiple of 6")
        except ValueError:
            print("Invalid input")

print(multiple_of_6())

