import fileinput #noqa

def line_value(line: str) -> int:
    return 0

def part2(data: str) -> int:
    return 0

def part1(data: str) -> int:
    return 0

if __name__ == "__main__":
    # Used to allow ipdb debugging by liberating the stdin
    with fileinput.input() as lines:
        data: str = "".join(lines)

    print(f'Part1 solution is {part1(data)}')
    print(f'Part2 solution is {part2(data)}')
