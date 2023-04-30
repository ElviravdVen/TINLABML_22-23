circle0 = Circle(10, "purple")  #!/usr/bin/env python

from shapes import Rectangle, Circle

rectangle1 = Rectangle(1, 2)
print(f"The area of the rectangle is : {rectangle1.getArea()}")

rectangle2 = Rectangle(2, 1)
print(f"The area of the rectangle is : {rectangle2.getArea()}")

# Test Addition
# rectangle1 -> self
# rectangle2 -> other
combinedArea = rectangle1 + rectangle2
print(f"The Combined area of the rectangle1 and rectangle2 is : {combinedArea}")

# Test Comparison
# rectangle1 -> self
# rectangle2 -> other
if rectangle1 == rectangle2:
    print("The area of rectangle1 equals the area of rectangle2")

circle0 = Circle(10, "purple")
