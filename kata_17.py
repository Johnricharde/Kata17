def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            pairs.append(s[i:i+2])
        else:
            pairs.append(s[i] + '_')
    return pairs