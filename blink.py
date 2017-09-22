def blink(states, B):
    # the main strategy is to use Binary XOR Operation
    
    # record the number of bulbs
    length = '0' + str(len(states)) + 'b'
    
    # make a string for state of bulbs
    current_ = ''
    for s in states:
        current_ += str(s)
    add_ = add(current_)
    loop = []

    while current_ not in loop:
        loop.append(current_)
        current_ = format(int(current_, 2) ^ int(add_, 2), length)
        add_ = add(current_)

    # remove the initial states
    loop = loop[1:]

    # get the position
    index = (B % len(loop)) - 1
    
    # if all bulbs are off, be careful
    if ('1' not in loop[-1]) & (B >= len(loop)):
        return  [int(s) for s in loop[-1]]
    else:
        return [int(s) for s in loop[index]]

def add(current_):
    # the strategy to turn on light
    # in this case, check the bulbs to the left
    
    return current_[-1] + current_[0:-1]

# test the function by command line
# example: python blink.py [1, 0, 0] 2

import sys
import ast

states = ast.literal_eval(sys.argv[1])
B = int(sys.argv[2])

print(blink(states, B))
