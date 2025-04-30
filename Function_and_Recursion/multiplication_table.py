n = int(input("Enter the number of that u want to create a multiplication table: "))
def multiplication_table(n):
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(n)