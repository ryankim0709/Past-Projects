class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def onCampus(self):
        self.here = True
        return self.here
    
    def offCampus(self):
        self.here = False
    
class Parent(Person):
    def __init__(self, name, age, numKids, nameKids):
        Person.__init__(self, name, age)
        self.numKids = numKids
        self.nameKids = nameKids
        
    def timeCampus(self, time):
        self.time = time

class Student(Person):
    def __init__(self, name, age, gradeLevel, gpa):
        Person.__init__(self, name, age)
        self.gradeLevel = gradeLevel
        self.gpa = gpa
        
    def updateGpa(self, newGpa):
        self.gpa = newGpa

class CSstudent(Student): 
    def __init__(self, name, age, earnings):
        self.earnings = earnings
        Student.__init__(self, name, age, 12, 7.89)
    
    def changeEarnings(self, newEarnings):
        self.earnings = newEarnings


best = CSstudent("Ryan", 14, 100000000000000000000000)
print(best.onCampus())