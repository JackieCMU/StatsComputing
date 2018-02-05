def multiply(num1, num2):
    res = [0]*len(num1+num2)
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            right, left = i + j + 1, i + j
            mul = int(num1[i])*int(num2[j])
            sum_ = mul + res[right]
            res[left] += sum_ // 10
            res[right] = sum_ % 10
    return str(sum([res[i]*10**(-i-1) for i in range(-1, -len(res)-1, -1)]))
