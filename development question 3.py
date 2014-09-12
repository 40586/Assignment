#Kieran Burentt
#12-09-2014
#Development


height_inch = float(input(" Please enter your height in inches: "))
weight_stone = float(input(" Please enter your weight in stone: "))

height_centi = height_inch * 2.54
weight_kilo = weight_stone * 6.364

print(" You weigh {0} Kilograms and you are {1} centimeters tall ".format(weight_kilo, height_centi))
