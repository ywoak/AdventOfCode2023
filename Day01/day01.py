import sys

NUMBERS = '123456789'

def part2():
    pass

def get_first(line: str) -> str:
    for char in line:
        if char in NUMBERS:
            return char

def part1(input: str) -> int:
    lines = input.splitlines()
    acc = 0
    for line in lines:
        first: str = get_first(line)
        last: str = get_first(line[::-1])
        total = int(first + last)
        acc += total
        print(f'{total =}')
    return (acc)
        

if __name__ == "__main__":
    res:int = part1(sys.stdin.read())
    print(f'Part1 solution is {res}')
