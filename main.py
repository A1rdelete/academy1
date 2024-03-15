#class Student:
#    name="A1rdelete"
#    def __init__(self):
#        self.name="a1rdelete"
#        self.age="14"
#        self.height = 180


#student1=Student()

#print(student1.name)
#Student.__init__(self=student1)


class Student:
    def __init__(self):
        self.height = 170

    height = 160

    def printer(self):
        print(self.height)


nick = Student()
nick.printer()


import random