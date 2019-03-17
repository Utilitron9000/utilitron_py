from typing import List, Callable
import random
from enum import Enum


def select_weighted_random(choices: List, top_x: int, utility_key: Callable):
    """Perform a weighted random selection from the top_x choices
    with the highest utility values"""
    top = get_top_x(choices, top_x, utility_key)
    weighted = get_weighted(top, utility_key)
    return weighted[random.randint(0, len(weighted) - 1)]


def get_top_x(choices: List, x: int, utility_key: Callable):
    """Get a list of x or fewer choices with the highest utility"""
    return sorted([i for i in choices],
                  reverse=True,
                  key=utility_key)[:x]


def get_weighted(choices: List, utility_key: Callable):
    """Repeat each choice 100 times for each utility point
    that it has"""
    weight_groups = [[c] * int(utility_key(c) * 100) for c in choices]
    return [c for group in weight_groups for c in group]


class SelectionMethod(Enum):
    MAX = 1
    WEIGHTED_RANDOM = 2
