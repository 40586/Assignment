#Kieran Burnett
#18-09-2014
#Denary to binary

denary_value = int(input("Please enter a denary number: "))

binary = ""
while denary_value > 0:
    binary = str(denary_value % 2) + binary
    denary_value = denary_value // 2

print("The bianry equivalent is {0} ".format(binary))

first_four = binary[0:4]

#Buggered up binary numbers needs fixing
if first_four == 0001
    print("The hexadecimal equivalent is 1 ")
if first_four == 0010
    print("The hexadecimal equivalent is 2 ")
if first_four == 0011
    print("The hexadecimal equivalent is 3 ")
if first_four == 0100
    print("The hexadecimal equivalent is 4 ")
if first_four == 0101
    print("The hexadecimal equivalent is 5 ")
if first_four == 0110
    print("The hexadecimal equivalent is 6 ")
if first_four == 0111
    print("The hexadecimal equivalent is 7 ")
if first_four == 1000
    print("The hexadecimal equivalent is 8 ")
if first_four == 1001
    print("The hexadecimal equivalent is 9 ")
if first_four == 1010
    print("The hexadecimal equivalent is A ")
if first_four == 1001
    print("The hexadecimal equivalent is B ")
if first_four == 1010
    print("The hexadecimal equivalent is C ")
if first_four == 1011
    print("The hexadecimal equivalent is D ")
if first_four == 110
    print("The hexadecimal equivalent is E ")
