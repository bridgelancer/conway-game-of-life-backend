import pytest

from app import INIT_CELL
from engine.conway import *


@pytest.fixture
def default_board():
    board = []
    for i in range(4):
        board.append([])
        for _ in range(4):
            board[i].append(INIT_CELL)
    return board


# Board initialization for common patterns

# Still lives patterns
block = [(0, 0), (0, 1), (1, 0), (1, 1)]
beehive = [(1, 1), (1, 2), (2, 0), (2, 3), (3, 1), (3, 2)]
loaf = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 3), (3, 2)]
boat = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)]
tub = [(0, 1), (1, 0), (1, 2), (2, 1)]
well = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)]


# Two period oscillators
blinker = [(1, 0), (1, 1), (1, 2)]
toad = [(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)]
beacon = [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)]


def modifiy_board(request, default_board):
    grid = default_board
    fixed_state = {'color': '#000000', 'fixed': True}

    for r, c in request.param:
        grid[r][c] = fixed_state

    return grid


@pytest.fixture(params=[block, beehive, loaf, boat, tub, well])
def still_lives(request, default_board):
    return modifiy_board(request, default_board)


@pytest.fixture(params=[blinker, toad])
def two_cycles_oscillators(request, default_board):
    return modifiy_board(request, default_board)


def test_still_lives(still_lives):
    board = convert_current_grid(still_lives)
    assert board == still_lives


def test_two_cycles_oscillators(two_cycles_oscillators):
    grid = two_cycles_oscillators

    first_period = convert_current_grid(grid)
    second_period = convert_current_grid(first_period)
    third_period = convert_current_grid(second_period)
    assert grid == two_cycles_oscillators
    assert first_period == third_period
