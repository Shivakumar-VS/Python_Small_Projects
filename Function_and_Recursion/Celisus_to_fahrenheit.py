f = int(input("Enter the temparature in F: "))

def f_to_c(f):
    return 5*(f-32)/9
c = f_to_c(f)
print(round(f_to_c(f),2), "celsius")