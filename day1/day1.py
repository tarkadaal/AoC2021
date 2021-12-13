def nwise(n, data):
    storage = []
    for item in data:
        storage.append(item)
        if len(storage) > n:
            storage = storage[1:]
        if len(storage) == n:
            yield storage


def count_increases(sequence):
    previous = None
    bigger = 0
    for depth in sequence:
        if previous is not None:
            bigger += 1 if depth > previous else 0
        previous = depth
    return bigger


def solve_part_1(data):
    return count_increases(data)


def solve_part_2(data):
    triplets = nwise(3, data)
    return count_increases((sum(x) for x in triplets))


if __name__ == "__main__":
    import os

    script_directory = os.path.dirname(__file__)
    input_path = os.path.join(script_directory, "input")

    ints = None
    with open(input_path) as input:
        ints = [int(x) for x in input]
    pt1 = solve_part_1(ints)
    print(f"Part 1: {pt1}")

    pt2 = solve_part_2(ints)
    print(f"Part 2: {pt2}")
