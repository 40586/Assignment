#Kieran Burnett
#22-09-2014
#Math unit exercises no2

#IMPORT
import math

#INPUT
pool_diameter = int(input(" Please enter the pools diameter: "))
pool_depth = int(input(" Please enter the pools depth: "))

#PROCESSING
pool_radius = pool_diameter / 2
area = math.pi * pool_radius**2
volume = area * pool_depth

#OUTPUT
print("The pools volume is: {0}".format(volume))
