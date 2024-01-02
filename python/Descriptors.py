class Descriptors:
    def __init__(self):
        self.__bmi = 0
    def __get__(self,instance,owner):
        return self.__bmi
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Bmi can only be an integer")

        if value < 0:
            raise ValueError("bmi can never be less than zero")

        self.__bmi = value

    def __delete__(self, instance):
        del self.__bmi

class Person:
    bmi = Descriptors()
    def __init__(self, name, age, bmi):
        self.name=name
        self.age=age
        self.bmi=bmi

    def __str__(self):
        return "{} age is {} and his bmi is {}".format(self.name, self.age, self.bmi)

person1 = Person("John", "25", 17)
#person1 = Person("John", "25", -17)
print(person1)
#person1.bmi=-10
#person1.bmi="John"

person2=Person("John", "25", 48)
print(person2)
print(person1)

# the descriptors are basically linked to a class and they are not linked to the instance
