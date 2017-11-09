import sys
import ast
from mapif import *

s = ast.literal_eval(sys.argv[1])
size = int(sys.argv[2])
step = int(sys.argv[3])

print(partition(s, size, step))
