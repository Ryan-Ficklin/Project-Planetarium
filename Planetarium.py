from Planet import Planet

class Planetarium(object):
    def __init__(self):
        self.mercury = Planet("Mercury", 3031, 32548000, 0)
        self.venus = Planet("Venus", 7521, 66871000, 0)
        self.earth = Planet("Earth", 7917, 92009000, 1)
        self.mars = Planet("Mars", 4222, 142120000, 2)
        self.jupiter = Planet("Jupiter", 86881, 484260000, 67)
        self.saturn = Planet("Saturn", 72367, 930450000, 62)
        self.uranus = Planet("Uranus", 31518, 1841600000, 27)
        self.neptune = Planet("Neptune", 30599, 2781900000, 14)
    def __str__(self):
        return f'''{self.mercury}
{self.venus}
{self.earth}
{self.mars}
{self.jupiter}
{self.saturn}
{self.uranus}
{self.neptune}'''
        
