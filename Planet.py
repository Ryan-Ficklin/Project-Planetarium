class Planet(object):
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
    def __str__(self):
        return f'''Name: {self.name},
Diameter: {self.diameter} miles,
Distance from Sun: {self.distance} miles,
Moons: {self.moons} '''
