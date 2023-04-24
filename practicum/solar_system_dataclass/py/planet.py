from dataclasses import dataclass, fields


@dataclass
class Planet:
    name: str
    diameter: float
    mass: float
    inclination: float
    eccentricity: float
    semiMajorAxis: float
    surfaceGravity: float
    orbitalPeriod: float
    siderealRotation: float
    satellites: int


planetDict = {"name": "Mars", "satellites": 0}
planet = Planet(planetDict.get('name'), planetDict.get('satellites1'))
print(planet)
