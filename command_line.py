# test the function by command line
import sys
import ast
from cutting_sticks import *

stick_length = int(sys.argv[1])
cuts = ast.literal_eval(sys.argv[2])

# plug in a list and an integer
print(best_cuts(stick_length, cuts)[1])
