import sys

NUMBERS = '123456789'
NUMLETTERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
NUMLETTERS_REV = [word[::-1] for word in NUMLETTERS]

def get_first_p2(line: str, rev: bool = False) -> str | None :
    numl: list[str] = NUMLETTERS_REV if rev else NUMLETTERS
    numl_first: list[str] = [num[0] for num in numl]

    for index, char in enumerate(line):
        if char in NUMBERS:
           return(char)
        if char in numl_first:
            numl_indices: list[int] = [i for i, elem in enumerate(numl_first) if elem == char]
            for numl_index in numl_indices:
                if (line[index: index + len(numl[numl_index])] == numl[numl_index]):
                    return NUMBERS[numl_index]
    return None

def part2(input: str) -> int:
    acc: int = 0

    for line in input.splitlines():
        first: str | None = get_first_p2(line)
        last: str | None = get_first_p2(line[::-1], rev=True)
        if first and last:
            total: int = int(first + last)
        acc += total
    return acc

def get_first(line: str) -> str | None:
    for char in line:
        if char in NUMBERS:
            return char
    return None

def part1(input: str) -> int:
    acc: int = 0

    for line in input.splitlines():
        first: str | None = get_first(line)
        last: str | None = get_first(line[::-1])
        total: int = 0
        if first and last:
            total = int(first + last)
        acc += total
    return (acc)

if __name__ == "__main__":
    input: str = sys.stdin.read()

    print(f'Part1 solution is {part1(input)}')
    print(f'Part2 solution is {part2(input)}')
