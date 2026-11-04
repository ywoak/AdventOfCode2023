import sys

NUMBERS = '123456789'
NUMLETTERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
NUMLETTERS_REV = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def get_first_p2(line: str, rev: bool = False) -> str :
    numl = NUMLETTERS_REV if rev else NUMLETTERS
    numl_first = [num[0] for num in numl]

    for index, char in enumerate(line):
        if char in NUMBERS:
           return(char)
        elif char in numl_first:
            numl_indices = [i for i, elem in enumerate(numl_first) if elem == char]
            for numl_index in numl_indices:
                if (line[index: index + len(numl[numl_index])] == numl[numl_index]):
                    return NUMBERS[numl_index]

def part2(input: str) -> int:
    acc: int = 0

    for line in input.splitlines():
        first: str = get_first_p2(line)
        last: str = get_first_p2(line[::-1], rev=True)
        total: int = int(first + last)
        acc += total
    return acc

def get_first(line: str) -> str:
    for char in line:
        if char in NUMBERS:
            return char

def part1(input: str) -> int:
    acc = 0

    for line in input.splitlines():
        first: str = get_first(line)
        last: str = get_first(line[::-1])
        total = int(first + last)
        acc += total
    return (acc)

if __name__ == "__main__":
    input: str = sys.stdin.read()

    print(f'Part1 solution is {part1(input)}')
    print(f'Part2 solution is {part2(input)}')
