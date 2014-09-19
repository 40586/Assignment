#Kieran Burnett
#19-09-2014
#we need if's

amount = int(input("please enter amount: "))

twenty_am = amount // 20
amount = amount % 20

ten_am = amount // 10
amount = amount % 10

five_am = amount // 5
amount = amount % 5

two_am = amount // 2
amount = amount % 2

one_am = amount // 1

print(" £20: {0}, £10: {1}, £5: {2}, £2: {3}, £1: {4}".format(twenty_am,ten_am,five_am,two_am,one_am))

