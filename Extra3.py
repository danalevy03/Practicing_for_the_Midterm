#Create a text file named "my_file.txt".
#Write a sentence to the file. Open and read the content from the file, then print it.

with open("my_file.txt", "w") as file:
    file.write("This is a sentence.")

with open("my_file.txt", "r") as file:
    print(file.read())




