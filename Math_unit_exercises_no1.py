#Kieran Burnett
#19-09-2014
#Math unit exercises no1

#IMPORTS
import math

#INPUTS
radius = int(input(" Please enter the radius of your circle: "))

#PROCESSING

radius2 = radius * 2
circumference = math.pi * radius2

area = math.pi * radius**2

#OUTPUTS
print(" The circumference of the circle is: {0:.2f} The area is: {1:.2f}".format(circumference,area))
