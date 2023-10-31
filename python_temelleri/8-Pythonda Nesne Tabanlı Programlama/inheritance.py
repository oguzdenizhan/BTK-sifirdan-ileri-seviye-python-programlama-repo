#inheritance (kalıtım) : Miras alma

# Person => name, lastname, age,eat(),run(),drink()
#Student(person),Teacher(person)

#animal =Dog(animal),cat(animal)

class Person():
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname
        print("Person Created")
    def who_am_i(self):
        print("i am a person")

    def eat(self):
        print("i am eating")

class Student(Person):

    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("Student Created")
    #override
    def who_am_i(self):
        print("i am a student")

    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch}teacher")

p1 = Person("Ali","Yılmaz")
s1 = Student("Çınar","Turan",1256)
t1 = Teacher("Oğuzhan","Denizhan","biology")

t1.who_am_i()
print(p1.firstname +" "+p1.lastname)
print(s1.firstname +" "+s1.lastname+ " "+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()