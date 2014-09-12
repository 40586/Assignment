#Kieran Burentt
#12-09-2014
#Development


fahrenheit = int(input("Please enter the temperture in fahrenheit: "))

stage_one = fahrenheit - 32
stage_two = 5 / 9
stage_three = stage_one * stage_two

print(" {0} Centigrade ".format(stage_three))
