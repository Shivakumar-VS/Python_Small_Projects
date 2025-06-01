#self refers to instance of a class
class Employee:
    language = "Kannada"
    salary = 100000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good Morning!")

shiva = Employee()
shiva.language = "Javascript"
shiva.greet()
shiva.getInfo() #Employee.getInfo(shiva)

#Instance attribute take preferences over class attributes during assignments and retrieval