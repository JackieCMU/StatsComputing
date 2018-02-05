def decodeString(s):
    stack = []
    res = ""
    for ss in s:
        if ss != "]":
            stack.append(ss)
        else:
            char, num = "", ""
            while stack and not stack[-1].isdigit():
                char += stack.pop()
            while stack and stack[-1].isdigit():
                num += stack.pop()
            char = char[::-1][1:]
            num = num[::-1]
            if stack:
                stack.extend(list(int(num)*char))
            else:
                res += int(num)*char
    res += ''.join(stack)
    return res
