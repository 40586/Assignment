# Kieran Burnett
# 23-09-2014
# Spot check program 2

weight = int(input(" Please enter the weight in grams: "))

one_hun = weight // 100
weight = weight % 100

fifty = weight // 50
weight = weight % 50

ten = weight // 10
weight = weight % 10

five = weight // 5
weight = weight % 5

two = weight // 2
weight = weight % 2

one = weight // 1
weight = weight % 1

print(" 100g = {0}, 50g = {1}, 10g = {2}, 5g = {3}, 2g = {4}, 1g = {5}".format(one_hun,fifty,ten,five,two,one))
