# Kieran Burnett
# 23-09-2014
# Assignment statement spot check

import math

pool_width = int(input(" Please enter the pools width: "))
pool_length = int(input(" Please enter the pools length: "))
pool_depth = int(input(" please enter the pools depth: "))

main_sec_vol = pool_length * pool_width * pool_depth
radius = pool_width / 2
cir_area = math.pi * radius**2
half_cir_vol = (cir_area / 2) * pool_depth
pool_volume = main_sec_vol + half_cir_vol

print(" The volume of the pool is: {0}".format(pool_volume))
