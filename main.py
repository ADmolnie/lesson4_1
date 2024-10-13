class Student1:
    color = "brown"
    student_brand = "student"

    def go(self):
        print("Let's go")

    def studing(self):
        print("Studiiing")

    def home(self):
        print("GO")

class Cat:
    def __init__(self, year, color, miofgh = "miofg"):
        self.year = year
        self.color = color 
        self.miofgh = miofgh

    name = "Zubenko Mikhail Petrovich"
    feel = "YAAAAAA"

    def jump(self):
        print("YEY", self.miofgh)

    def scream(self):
        print("AAAAAA, I AM", self.color)

    def boring(self):
        print("boriiiing(he is", self.year, "old)")

student1 = Student1()
cat = Cat(year = 13, color = "I")

print(student1.student_brand)
print(cat.feel)

student1.home()
cat.boring()
cat.scream()
cat.jump()