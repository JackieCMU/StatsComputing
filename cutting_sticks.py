# the subproblem:
# f(start, end) = min{(end - start) + f(start, cut) + f(cut, end)}
# for all cut points
# if start < end: continus  
# elif start is next to end: return 0
# else: return min{(end - start) + f(start, cut) + f(cut, end)}

def best_cuts(stick_length, cuts):
 
    import numpy as np

    len1 = 2 + len(cuts)
    add = [0] + cuts + [stick_length]
    cost = np.full((len1 + 1, len1 + 1), np.inf)
    method = np.full((len1 + 1, len1 + 1), '', dtype = np.object)

    cost[0, 0] = 0
    for i in range(len1):
        cost[i + 1, 0] = add[i]
        cost[0, i + 1] = add[i]

    for i in range(len1):
        method[i + 1, 0] = str(add[i])
        method[0, i + 1] = str(add[i])

    for row in range(len1, 0, -1):
        for col in range(1, len1  + 1):
            if row >= col:
                continue
            elif (row + 1) == col:
                cost[row, col] = 0
            else:
                min_ = []
                pos = []
                for start in range(row + 1, col):
                    min_.append((cost[0, col] - cost[row, 0]) + cost[row, start] + cost[start, col])
                    pos.append(start)
                cost[row, col] = min(min_)
                ind = min_.index(min(min_))
                method[row, col] = str(method[0, pos[ind]]) + '|'  + method[row, pos[ind]] + '|' + method[pos[ind], col]
	
	# take out the number
    strategy = method[1, len1].split('|')
    strategy = [int(num) for num in strategy if len(num) != 0 ]
    return (int(cost[1, len1]), strategy)
