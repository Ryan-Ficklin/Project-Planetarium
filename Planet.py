class Planet(object):
    def __init__(self, name, diameter, distance, rings):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.rings = rings
    def __str__(self):
        return f'''Name: {self.name},
Diameter: {self.diameter},
Distance from Sun: {self.distance},
Rings: {self.rings} '''
