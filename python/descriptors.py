class Person:
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi
        if self.bmi < 0:
            raise ValueError("Bmi can never be less than zero")
        if isinstance(self.name, str):
            print(self.name)
        else:
            raise ValueError("Name of the person can never be an integer")

    def __str__(self):
        return "{} age is {} with a bmi of {}".format(self.name, self.age, self.bmi)

person1 = Person("John", "25", 17)
#person1 = Person(10, "25", 17)
print(person1)
person1.name = 10
person1.bmi = -10
print(person1)

#person2 = Person("John", "25", -17)
#print(person2)
