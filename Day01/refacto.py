#import sys
import fileinput

NUMLETTERS: tuple[str, ...] = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
NUMLETTERS_REV: tuple[str, ...] = tuple(word[::-1] for word in NUMLETTERS)

def get_first_elem(line: str, rev: bool = False, p2: bool = False) -> str | None:
    numl: tuple[str, ...] = NUMLETTERS_REV if rev else NUMLETTERS

    for index, char in enumerate(line):
        if char.isdigit(): #leaves out the 0 case, but unecessary for this one
            return char
        if p2:
            for i_num, num in enumerate(numl, start=1):
                if line.startswith(num, index): #old line[index:], but add a copy each run
                    return str(i_num)

    return None

def line_value(line: str, p2: bool) -> int:
    first: str | None = get_first_elem(line, p2=p2)
    last: str | None = get_first_elem(line[::-1], rev=True, p2=p2)

    if first and last:
        return int(first + last)
    return 0

def solve(data: str, p2: bool = False) -> int:
    '''
    Old acc += total, total = first + last
    Generator + sum is more pytonic and crisps
    '''
    return sum (line_value(line, p2) for line in data.splitlines())

if __name__ == "__main__":
    #data: str = sys.stdin.read()

    # Used to allow ipdb debugging by liberating the stdin
    with fileinput.input() as lines:
        data: str = "".join(lines)

    print(f'Part1 solution is {solve(data)}')
    print(f'Part2 solution is {solve(data, p2=True)}')
