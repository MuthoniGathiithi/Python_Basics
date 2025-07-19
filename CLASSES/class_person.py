class Person:
    def __init__(self, name, age,school, address):
        self.name = name
        self.age = age
        self.school = school
        self.address = address

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, I study at {self.school}, and I live at {self.address}."
    
p1 = Person("Joyce",20,"KCAU UNIVERSITY","Nairobi, Kenya")
print(p1.introduce())