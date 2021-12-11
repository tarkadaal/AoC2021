with open('input') as input:
    previous = None
    bigger = 0
    for line in input:
        depth = int(line)
        if previous is not None:
            bigger += 1 if depth > previous else 0
        previous = depth
    print(bigger)
