def compress(chars):
    anchor = write = 0
    for read, v in enumerate(chars):
        if read + 1 == len(chars) or chars[read+1] != v:
            chars[write] = chars[read]
            write += 1
            if read > anchor:
                for d in str(read - anchor + 1):
                    chars[write] = d
                    write += 1
            anchor = read + 1
    return chars



    s = collections.Counter(chars)
    count = 0
    for d in s:
        if s[d] != 1:
            count += len(str(s[d]))
        count += 1
    return count
