# Kieran Burnett
# 24-09-2014
# Selection R&R

age = int(input(" Please enter your age: "))

if age >= 18:
    print(" You are old enough to vote")
if age < 18:
    print(" You are not old enough to vote")
age = 65 - age

if age <= 0:
    print(" You can retire!")
if age > 0:
    print(" You can retire in {0} years!".format(age))
