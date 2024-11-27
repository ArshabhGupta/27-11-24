file = open('text.txt', 'r')
print("File in read mode!")
print(file.read())
file.close()

file = open('text.txt', 'w')
file.write("File in the write mode.....")
file.write("Hello I am Arshabh!")
file.close()

file = open('text.txt', 'a')
file.write("File in the append mode.....")
file.write("Hello World")
file.close()