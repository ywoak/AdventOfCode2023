import re
from itertools import product

NEIGHBORS: list[tuple[int, ...]] = [d for d in product((-1, 0, 1), repeat=2) if d != (0, 0)]

def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
