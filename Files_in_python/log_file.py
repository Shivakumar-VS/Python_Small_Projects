with open("log_file.html") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No python is not present")
