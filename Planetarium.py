from Planet import Planet

class Planetarium(object):
    def __init__(self):
        self.create()
    def __str__(self):
        return f'''{self.planets[0]}
{self.planets[1]}
{self.planets[2]}
{self.planets[3]}
{self.planets[4]}
{self.planets[5]}
{self.planets[6]}
{self.planets[7]}'''
    def create(self):
        self.planets = []
        self.planets.append(Planet("Mercury", 3031, 32548000, 0))
        self.planets.append(Planet("Venus", 7521, 66871000, 0))
        self.planets.append(Planet("Earth", 7917, 92009000, 1))
        self.planets.append(Planet("Mars", 4222, 142120000, 2))
        self.planets.append(Planet("Jupiter", 86881, 484260000, 67))
        self.planets.append(Planet("Saturn", 72367, 930450000, 62))
        self.planets.append(Planet("Uranus", 31518, 1841600000, 27))
        self.planets.append(Planet("Neptune", 30599, 2781900000, 14))
    def printOne(self):
        planetChoice = str(input('''Which planet would you like to review?
(Please capitalize the first letter) '''))
        length = len(self.planets)
        for i in range(length):
            if(self.planets[i].name == planetChoice):
                print(str(self.planets[i]))
                           
