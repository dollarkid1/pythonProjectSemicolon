class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name


p = Person("Dan", "Foster", 19, "male")
print(p.get_first_name())
p.set_first_name("Ghost")
print(p.get_first_name())
