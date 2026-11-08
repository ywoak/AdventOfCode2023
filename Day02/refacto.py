import fileinput #noqa
import math

GOAL: dict[str, int] = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solve(game: str) -> int:
    game_id: int = int(game.split(':')[0].split()[-1])
    rgb: dict[str, int] = get_max_occurrence(game)
    possible: bool = all(rgb[color] <= limit for color, limit in GOAL.items())
    return game_id if possible else 0

def get_max_occurrence(game: str) -> dict[str, int]:
    rgb: dict[str, int] = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    game_sets = game.split(':')[1].strip().split(';')
    for game_set in game_sets:
        for dice in game_set.split(','):
            num, color = dice.split()
            rgb[color] = max(rgb[color], int(num))

    return rgb

def part2(games: str) -> int:
    return sum(math.prod(get_max_occurrence(game).values()) for game in games.splitlines())

def part1(games: str) -> int:
    return sum(solve(game) for game in games.splitlines())

if __name__ == "__main__":
    # Used to allow ipdb debugging by liberating the stdin
    with fileinput.input() as lines:
        data: str = "".join(lines)

    print(f'Part1 solution is {part1(data)}')
    print(f'Part2 solution is {part2(data)}')
