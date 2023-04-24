#!/usr/bin/env python3

class Planet:
    def __init__(self, mass, diameter, inclination):
        self.mass = mass
        self.diameter = diameter
        self.inclination = inclination

mercury = Planet(mass=3.302,diameter=4879.4,inclination = 7.004000)

print(mercury.mass)

# *10^23
# mercury.mass = 3.302
# mercury.diameter = 4879.4
# mercury.inclination = 7.004000
