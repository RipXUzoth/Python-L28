class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
     print("Name: ", self.name)
     print("ID Number: ", self.id_number)
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post
emp = Employee("Rahul", "E14353C", 50000, "Software engineer")
emp.display()