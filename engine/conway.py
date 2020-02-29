from engine.color import color_mean
"""Module to provide functions to compute next state by the Conway rules.

The rules are stated here for a reference.

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

"""
def compute_life_cell(neighbour_cells):
    life_cells = [cell for cell in neighbour_cells if cell['fixed']]
    if len(life_cells) < 2 or len(life_cells) > 3:
        return '#ffffff', False
    else:
        return color_mean([cell['color']for cell in life_cells]), True

def compute_dead_cell(neighbour_cells):
    life_cells = [cell for cell in neighbour_cells if cell['fixed']]
    if len(life_cells) == 3:
        return color_mean([cell['color'] for cell in life_cells]), True
    else:
        return '#ffffff', False

def extract_neighbour_cell(row, col, grid):
    num_of_row = len(grid)
    num_of_col = len(grid[0])

    # refactor this
    neighbour_cells = []
    for r in [row-1, row, row+1]:
        if 0 <= r <= num_of_row-1:
            for c in [col-1, col, col+1]:
                if 0 <= c <= num_of_col-1:
                    if not(r == row and c == col):
                        neighbour_cells.append(grid[r][c])
    return neighbour_cells


def convert_current_grid(grid):
    new_grid = []
    for r, row in enumerate(grid):
        new_grid.append([])
        for c, cell in enumerate(row):
            neighbour_cells = extract_neighbour_cell(r, c, grid)
            # might also alter color within functions
            if cell['fixed']:
                color, fixed = compute_life_cell(neighbour_cells)
            else:
                color, fixed = compute_dead_cell(neighbour_cells)
            new_grid[r].append({'color': color, 'fixed': fixed})

    return new_grid
