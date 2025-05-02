words  = ["Donkey", "bad", "ganda"]

with open("Donkey1.txt" ,"r") as f:
    content = f.read()

for word in words:
    content= content.replace(word, "#" * len(word))

with open("Donkey1.txt" ,"w") as f:
    f.write(content)