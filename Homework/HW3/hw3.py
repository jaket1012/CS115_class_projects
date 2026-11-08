# === CS 115 Homework 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 3 ===
def no_rows(m):
    """creates a list of m empty lists"""
    if m == 0:
        return []
    return [[]] + no_rows(m-1)
def empty_row(m):
    """creates a row with m columns of 0s"""
    if m==0:
        return []
    if m==1:
        return [0]
    return [0] + empty_row(m-1)
    
def empty(m, n):
    """returns an mxn grid of all 0s"""
    if n == 0:
        return no_rows(m)
    if n == 1:
        return [empty_row(m)]
    return [empty_row(m)] + empty(m,n-1)

def copy_row(grid):
    """creates a deep copy of the inputted row"""
    if len(grid)== 0:
        return []
    new_value = 1*grid[0]
    return [new_value] + copy_row(grid[1:])
        
def copy(grid):
    """creates a deep copy of the inputted grid"""
    if len(grid) == 0:
        return []
    if len(grid) == 1:
        return [copy_row(grid[0])]
    else:
        return [copy_row(grid[0])] + copy(grid[1:])

def add_to_row(row, cost):
    """adds cost to each item in a row and returns that row"""
    if len(row) == 0:
        return []
    else:
        new_value = row[0] + cost
        return [new_value] + add_to_row(row[1:], cost)

def increase_row(grid, y, cost):
    """increases each item in the y row by cost"""
    grid[y] = add_to_row(grid[y],cost)

def add_to_col(grid, x, cost):
    """creates a new grid but the x item in each row is increased by cost"""
    if grid == []:
        return []
    else:
        grid[0][x] += cost
        return add_to_col(grid[1:], x, cost)

def increase_col(grid, x, cost):
    """sets grid to a new grid were each item in the x column is increased by cost"""
    grid = add_to_col(grid, x, cost)
    
def distance_from(grid, x, y):
    """returns the smallest distance from a place in the grid (x,y) from (0,0)"""
    memo = {}
    def _distance_from(grid, x, y):
        if x == 0 and y == 0:
            return grid[0][0]
        if (x,y) in memo:
            return memo[(x,y)]
        if x == 0:
            memo[(x,y)] = grid[x][y] + distance_from(grid, x, y-1)
            return grid[x][y] + _distance_from(grid, x, y-1)
        elif y == 0:
            memo[(x,y)] = grid[x][y] + distance_from(grid, x-1, y)
            return grid[x][y] + _distance_from(grid, x-1, y)
        else:
            up = grid[x][y] + _distance_from(grid, x-1, y)
            left = grid[x][y] + _distance_from(grid, x, y-1)
            memo[(x,y)] = min(up, left)
            return min(up, left)
    return _distance_from(grid, x, y)


