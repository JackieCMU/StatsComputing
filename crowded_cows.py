# use hash table
# kick out the first one, add the new, key - ID, value - Position

def crowded_cows(cow_list, k):
    
    import collections as cl
    window_cows = cl.OrderedDict()  # window_cows: the cows with ID and position in the window
    maximal_id = -1
    length = len(cow_list)
    
    # make a hash table to record ID and position for the first k cows
    for i in range(k):
        if cow_list[i] in window_cows and cow_list[i] > maximal_id:
            window_cows[cow_list[i]] = i
            window_cows.move_to_end(cow_list[i])
            maximal_id = cow_list[i]
        elif cow_list[i] in window_cows:
            window_cows[cow_list[i]] = i
            window_cows.move_to_end(cow_list[i])
        else:
            window_cows[cow_list[i]] = i

    # move the window and record the new cow and remove the old one if condition is met
    for i in range(k, length):
        first_key = next(iter(window_cows.keys()))
        first_index = window_cows[first_key]
        if cow_list[i] in window_cows and cow_list[i] > maximal_id:
            # check whether the first (key, value) would be kicked out
            if i - first_index == k:
                window_cows.popitem(last=False)
            window_cows[cow_list[i]] = i
            window_cows.move_to_end(cow_list[i])
            maximal_id = cow_list[i]
        elif cow_list[i] in window_cows:
            if i - first_index == k:
                window_cows.popitem(last=False)
            window_cows[cow_list[i]] = i
            window_cows.move_to_end(cow_list[i])
        else:
            if i - first_index == k:
                window_cows.popitem(last=False)
            window_cows[cow_list[i]] = i

    return maximal_id

