#john bain
#05-09-12
#variable improvement exercise

import math

Radius = int(input("please enter the radius of the circle: "))

Cir = 2*math.pi*Radius
Cir = round(Cir,2)

Area = math.pi * Radius**2
Area = round(Area,2)

print("The circumference of this circle is: {0}.".format(Cir))
print("The area of this circle is: {0}.".format(Area))
