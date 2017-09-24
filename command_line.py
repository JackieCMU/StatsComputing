# test the function by command line
# example: python blink.py [1, 0, 0] 2
import sys
import ast 
from blink import blink
from blink import add

states = ast.literal_eval(sys.argv[1])
B = int(sys.argv[2])
 
print(blink(states, B)) 
