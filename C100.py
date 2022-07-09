class Plant(object):
    def __init__(self, colour, name, maxage, family, height):
        self.colour = colour
        self.name = name
        self.age = maxage
        self.family = family
        self.height = height

    def display (self):
        print("name: ",self.name)
        print("colour: ",self.colour)
        print("age: ",self.age)
        print("family: ",self.family)
        print("height: ",self.height)
        print("-----------------------------------------------------------")
        

neem = Plant("green", "Neem", "200 Years","Mahogany" , "20-40m")
peepal = Plant("green", "Peepal", "1500 Years","sacred fig" , "30m")

peepal.display()
neem.display()

