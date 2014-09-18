#Kieran Burnett
#18-09-2014
#making up for illness

#WARNING: doesnt work, need to be fixed

#INPUTS
pool_length = int(input(" Please enter the pools length: "))
pool_width = int(input(" Please enter the pools width: "))

deep = int(input(" Please enter the pools depth at its deepest: "))
shallow = int(input(" Please enter the pools depth at its shallowest: "))

deepend = int(input(" Please enter the length of the deepend: "))
shallowend = int(input(" Please enter the length of the shallowend: "))

#PROCESSING

#x
part1 = pool_length * pool_width * shallow

#y
part2 = deepend * deep * pool_width

#v
part3 = pool_length - deepend

#(d-s)
part4 = deepend - shallowend

#c
pool_slope = part3 - shallowend
#z
part5 = part4 * pool_slope * pool_width
part6 = part5 / 2

# x + y + z
final_sum = part1 + part2 + part6

#OUTPUT
print(" The volume of water required to fill the pool is: {0}".format(final_sum))


