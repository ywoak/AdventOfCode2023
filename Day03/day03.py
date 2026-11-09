import fileinput #noqa

NOT_SYMBOL: str = '.0123456789'

neighbor_8d: dict[str, tuple[int, int]] = {
    'EAST': (0, 1),
    'SE': (1, 1),
    'South': (1, 0),
    'SW': (1, -1),
    'West': (0, -1),
    'NW': (-1, -1),
    'North': (-1, 0),
    'NE': (-1, 1),
}

def get_number(index: int, line: list[str]) -> int:
    start: int = index
    end: int = index

    while start - 1 >= 0 and line[start - 1].isdigit():
        start -= 1

    while end + 1 < len(line) and line[end + 1].isdigit():
        end += 1

    return int("".join(line[start: end + 1]))

def is_symbol(nx: int, ny: int, grid: list[list[str]]) -> bool:
    # check out of bound first
    len_grid = len(grid)
    len_line = len(grid[0]) # It's a rectangle

    if nx < 0 or nx >= len_grid or ny < 0 or ny >= len_line:
        return False
    return grid[nx][ny] not in NOT_SYMBOL

def is_part_number(x: int, y: int, grid: list[list[str]]) -> bool:
    return any(is_symbol(nx + x, ny + y, grid) for nx, ny in neighbor_8d.values())

def part1(data: str) -> int:
    grid: list[list[str]] = list(map(list, data.splitlines()))
    acc = 0

    part_number_added = False
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if part_number_added and c.isdigit():
                continue
            part_number_added = False
            if c.isdigit() and is_part_number(x, y, grid):
                acc += get_number(y, line)
                part_number_added = True

    return acc

if __name__ == "__main__":
    # Used to allow ipdb debugging by liberating the stdin
    with fileinput.input() as lines:
        data: str = "".join(lines)

    print(f'Part1 solution is {part1(data)}')
