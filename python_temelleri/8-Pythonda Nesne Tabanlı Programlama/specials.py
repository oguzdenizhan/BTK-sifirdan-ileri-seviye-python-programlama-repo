mylist = [1,2,3]
myString = "my string"

# print(len(mylist))
# print(len(myString))

# print(type(mylist))
# print(type(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("movie silindi")
    


m= Movie("film adı","film yönetmeni",120)

# print(type(m))
# print(len(m))


# print(str(mylist))
# print(str(m))

print(len(mylist))
print(len(m))

# del m
# print(m)
