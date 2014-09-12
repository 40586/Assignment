#Kieran Burentt
#12-09-2014
#Development

def one():
    num1 = int(input("Please enter number one: "))
    num2 = int(input("PLease enter number two: "))
    
    Div = num1 // num2
    Mod = num1 % num2
    
    print(" {0} / {1} = {2} remainder = {3}".format(num1, num2, Div, Mod))
