# test the function by command line
import sys
import ast
from crowded_cows import crowded_cows

cow_list = ast.literal_eval(sys.argv[1])
k = int(sys.argv[2])

# plug in a list and an integer
print(crowded_cows(cow_list, k))
