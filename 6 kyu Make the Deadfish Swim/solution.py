def parse(data):
    number = 0
    result = []
    i  = lambda x: x + 1
    d  = lambda x: x - 1
    s  = lambda x: x ** 2
    o  = lambda x: result.append(x)
    for command in data:
        if command == 'i':
            number = i(number)
        elif command == 'd':
            number = d(number)
        elif command == 's':
            number = s(number)
        elif command == 'o':
            o(number)
    return result
