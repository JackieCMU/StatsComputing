def ValueIteration(state, k, theta, P, R, base):
    V = [base]
    for i in range(k):
        V.append([3])
        for j in range(1, len(base)-1):
            left = (R["left"][j] + theta*V[i][j-1])*P["left"][j]
            right = (R["right"][j] + theta*V[i][j+1])*P["right"][j]
            V[i+1].append(max(left, right))
        V[i+1].append(1)
    print(V)
    return V[k][state]

theta = 0.2
P = {"left" : [0, 1, 1, 1, 1, 1, 0],
     "right" : [0, 1, 1, 1, 1, 1, 0]}
R = {"left" : [0, 0, 0, 0, 0, 0, 0],
     "right" : [0, 0, 0, 0, 0, 0, 0]}
base = [3, 0, 0, 0, 0, 0, 1]

print(ValueIteration(1, 10, theta, P, R, base))
