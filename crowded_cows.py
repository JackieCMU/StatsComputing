def crowded_cows(cow_list, k):
    # hash table
    import collections as cl
    ht = cl.OrderedDict()
    maximal_ID = -1
    
    # make a hash table to record ID and position
    for pos, value in enumerate(cow_list[:k]):
        ht[value] = pos
    for pos, ID in enumerate(cow_list[k:]):
        if ((ID in ht) & (ID > maximal_ID)):
            ht.popitem(last = False)
            ht[ID] = pos
            ht.move_to_end(ID)
            maximal_ID = ID
        elif ID in ht:
            ht.popitem(last = False)
            ht[ID] = pos
            ht.move_to_end(ID)
        else:
            ht.popitem(last = False)
            ht[ID] = pos
    return maximal_ID

# test the function by command line
import sys
import ast

cow_list = ast.literal_eval(sys.argv[1])
k = int(sys.argv[2])

# plug in a list and an integer
print(crowded_cows(cow_list, k))
