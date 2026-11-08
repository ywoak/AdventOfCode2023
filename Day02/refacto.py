import fileinput #noqa
from operator import mul
from functools import reduce

goal = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solve_p2(game: str) -> int:
    return reduce(mul, get_max_occurence(game).values())

def solve(game: str) -> int:
    id: int = int(game.split(':')[0].split(' ')[-1])
    rgb: dict[str, int] = get_max_occurence(game)
    impossible: bool = False
    for color, num in goal.items():
        if rgb[color] > num:
            impossible = True
    return 0 if impossible else id

def get_max_occurence(game: str) -> dict[str, int]:
    rgb: dict[str, int] = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    sets = game.split(':')[1].strip().split(';')
    for set in sets:
        for dice in set.split(','):
            d_split = dice.strip().split(' ')
            color: str = d_split[1]
            num: int = int(d_split[0])
            rgb[color] = max(rgb[color], num)

    return rgb

def part2(games: str) -> int:
    return sum(solve_p2(game) for game in games.splitlines())

def part1(games: str) -> int:
    return sum(solve(game) for game in games.splitlines())

if __name__ == "__main__":
    # Used to allow ipdb debugging by liberating the stdin
    with fileinput.input() as lines:
        data: str = "".join(lines)

    print(f'Part1 solution is {part1(data)}')
    print(f'Part2 solution is {part2(data)}')
