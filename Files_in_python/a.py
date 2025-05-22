file = open("shivam.txt", "w")
file.write("Hello I am Shivakumar")
file.close()

file = open("shivam.txt")
s = file.read()
print(s)
file.close()