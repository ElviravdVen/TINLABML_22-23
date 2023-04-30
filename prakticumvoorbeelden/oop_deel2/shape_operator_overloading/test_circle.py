#!/usr/bin/env python

from circle import Circle

circle0 = Circle(10, "purple")
circle1 = Circle(10, "blue")

print(f"cirlcle0 color : {circle0.getColor()}")
print(f"cirlcle1 color : {circle1.getColor()}")

if circle0 != circle1:
    print("Circles are not the same")
else:
    print("Circles are the same")
