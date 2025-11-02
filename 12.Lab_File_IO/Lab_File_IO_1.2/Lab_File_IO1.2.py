# 1. input()
name = input("Enter your name: ")
print(f"Hello,{name}!")

# 2. print()
print("This is a print statement.")

# 3. open() and read()
file = open("example.txt","w")
file.write("First line of the file.\nSecond line of the file.")
file.close()

#4. Re-open the file to read it
file = open("example.txt","r")
content = file.read()
print("content read using read():")
print(content)
file.close()

# 5. readline()
file = open("example.txt","r")
line = file.readline()
print("First line read using readline():")
print(line)
file.close()

# 6. readlines()
file = open("example.txt","r")
lines = file.readlines()
print("Lines read using readlines():")
print(lines)
file.close()

# 7. write()
file = open("example.txt", "a")  # 'a' for append mode
file.write("\nThird line appended to the file.")
file.close()

# 8. writelines()
lines_to_write = ["Fourth line.\n", "Fifth line.\n"]
file = open("example.txt", "a")
file.writelines(lines_to_write)
file.close()

# 9. close()
file = open("example.txt", "r")
print("Content before closing the file:")
print(file.read())
file.close()
# After closing, the file cannot be read
# print(file.read())  # This would raise an error

# 10. flush()
file = open("example.txt","w")
file.write("This line will be written immediately.")
file.flush() # forces the write to happen immediately
file.close()

# 11. seek() and 12. tell()
file = open("example.txt","r")
print("Current file position:", file.tell())  # Outputs the position (should be 0)
file.seek(10)  # Move to the 10th byte
print("New file position after seek(10):", file.tell())
file.close()

# 13. truncate()
file = open("example.txt", "r+")
file.truncate(20)  # Truncate the file to 20 bytes
file.close()

# 14. with open() (context manager)
with open("example.txt", "r") as file:
    content = file.read()
    print("Content read using with open():")
    print(content)
# File is automatically closed after the block

