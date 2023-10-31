#class

class Person:
    
    #class attributes
    address="no information"

    #constructor (yapıcı metod)
    def __init__(this,name,year):

        #object attributes
        this.name= name
        this.year =year
        print("init metodu çalıştı")
        

    #methods
    #instance methods
    def intro(self):
        print("Hello There! I am "+self.name)
    def calculateAge(self):
        return 2023-self.year




#object,instance
# p1 = Person("ali",1990)
# p2 = Person(name="yağmur",year=1994)

#update
# p1.name="ahmet"
# p1.address="Malatya"

#accessing abject attributes
# print(f"p1 name {p1.name} year {p1.year} address {p1.address}")
# print(f"p2 name {p2.name} year {p2.year} address {p2.address}")

# print(p1)
# print(p2)
# print(type(p1))
# print(type(p2))
# print(p1==p2)

# p1.intro()
# p2.intro()

# print(f"Adım: {p1.name} yaşım {p1.calculateAge()}")
# print(f"Adım: {p2.name} yaşım {p2.calculateAge()}")


class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    
    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi *( self.yaricap**2)
    
c1 = Circle() #yaricap belirtmedik yukarıda tanımlamamıza göre yarıcap=1 olacak
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")