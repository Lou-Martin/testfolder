#test code here
class Mather():
    def __init__(self):
        self.number = (2 * 2)
    def return_number(self):
        return self.number

math_here = Mather()

class Players():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def return_fullname(self):
        return self.first_name + " " + self.last_name
    
player1 = Players("Louis", "Martin", 29)
player2 = Players("Jade", "Beadle", 30)

print(player2.return_fullname())
print(player1.age)

class Animal():
    def __init__(self, name, colour, dangerous, mood):
        self.name = name
        self.colour = colour
        self.dangerous = dangerous
        self.mood = mood

    def desribe_animal(self):
        return f"The {self.colour} {self.name}, a {self.mood} animal. Dangerous? {self.dangerous}."

cat = Animal("Cat", "black", "Sure is", "mischevious")
dog = Animal("Dog", "brown", "Only if you're a criminal", "loyal")
fox = Animal("Fox", "red", "If you're mean", "clever")

print(dog.desribe_animal())

test_list = [1,2,3,4]

def total(list):
    count = 0
    for i in list:
        count += i
    return count

print(total(test_list))

lowlist =  [4, 2, 6]
print(lowlist[1])
def lowest_number(list):
    list.sort()
    return list[0]

print(lowest_number(lowlist))

def remove_nones_from_list(list):
    for i in list:
        if i == None:
            list.remove(i)
        return list
