#To write in to a file using a open() built-in function
f = open("file.txt", "w")
f.write("Harry is a good boy")
f.close()

#read into a file ,, by default the file is in reading mode
f = open("file.txt")
data = f.read()
print(data)
f.close()
