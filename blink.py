# change bulbs' state for B times based on a certain rule
# in this case, rule is changing bulb's state if state of its left is 1
def blink(states, B):
    
    cur_state = {}
    
    for pos, state in enumerate(states):
        cur_state[pos] = state

    loop_state = []

# the states are limited and repeated
for i in range(B):
    add_state = blink_all(cur_state)
        
        # special case if all states are 0
        if 1 not in add_state:
            return add_state
    elif add_state in loop_state:
        break
        loop_state.append(add_state)

return loop_state[B % len(loop_state) - 1]

# change state once based on left bulb's state
def blink_once(left, cur):
    if left == 1:
        return 1 - cur
    else:
        return cur

# change all states
def blink_all(cur_state):
    length = len(cur_state)
    last = cur_state[length - 1]
    for pos in range(length - 1, 0, -1):
        cur_state[pos] = blink_once(cur_state[pos - 1], cur_state[pos])
    if last == 1:
        cur_state[0] = 1 - cur_state[0]
    return list(cur_state.values())
