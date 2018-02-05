def findMinDifference(timePoints):
    time = [int(t[:2])*60 + int(t[-2:]) for t in timePoints)]
    time.sort()
    time.append(time[0] + 1440)
    return min(b - a for a, b in zip(time[:-1], time[1:]))
