def inch_to_cms(inch):
    return inch * 2.34

n = int(input("Enter the value in inches: "))
print(f"The corresponding value in cms :", inch_to_cms(n))