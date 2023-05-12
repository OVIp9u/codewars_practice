def solution(s):
    result =[]
    for num in range(1, len(s), 2):
        item = f'{s[num-1]}{s[num]}'
        result.append(item)
    if len(s)%2 != 0:
        result.append(f'{s[-1]}_')
    return result
