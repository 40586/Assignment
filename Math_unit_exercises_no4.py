# Kieran Burnett
# 24-09-2014
# Math unit exercises

import math

distance = int(input(" Please enter the distance the plane traveled: "))
angle = int(input(" Please enter the angle the plane was traveling at: "))

answer_west = math.sin(angle) * distance
answer_east = math.cos(angle) * distance

print("the plane traveled {0}Km east and {1}Km north".format(answer_east, answer_west))
