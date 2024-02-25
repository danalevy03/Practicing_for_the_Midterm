
# Use an f-string to print a message with the current year.
from datetime import datetime

current_year = datetime.now().year
print(f"The current year is {current_year}.")

#Write a program that opens a file, writes a message, and closes the file.
with open("message.txt", "w") as file:
    file.write("Hello, World!")

closed = file.closed
print(closed)








