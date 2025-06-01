#self refers to instance of a class
class Employee:
    language = "Kannada"
    salary = 100000

    def __init__(self,name , salary, language):
        self.name = name
        self.salary = salary
        self.language=language
         #dunder method which is automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good Morning!")

shiva = Employee("Shivakumar", 130000, "JS")
# shiva.name = "Shivakumar"
print(shiva.name , shiva.salary, shiva.language)

# rohan = Employee()