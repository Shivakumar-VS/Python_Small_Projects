class Employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is ur language : {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} Language")

a=Employee()
b=Programmer()                                  

b.show()
b.printLanguage()
b.showLanguage()