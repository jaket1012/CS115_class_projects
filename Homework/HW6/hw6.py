# Name: Jake Talvy
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

def parse_file(filename):
    """turns a text file into a nested list if formatted correctly"""
    myfile = open(filename, "r")
    grid = []
    for line_of_text in myfile:
        row = []
        for item in line_of_text.split(" "):
            item = int(item)
            row += [item]
        grid += [row]
    expected_row_amt = grid[0][1]
    expected_col_amt = grid[0][0]
    if len(grid) - 1 != expected_row_amt or len(grid[1]) != expected_col_amt or len(grid[0]) != 2:
        print("list has incorect bounds or text file was not properly formatted")
        raise ValueError
    return grid[1:]


def accumulate_row_distance(lst):
    """takes the distance from the first item in the row including the current item and turns it into a list"""
    new_lst = []
    for item in range(len(lst)):
        if item == 0:
            new_lst += [lst[item]]
            continue
        new_lst += [lst[item] + new_lst[item-1]]
    return new_lst

def accumulate_col_distance(grid, col):
    """takes the distance from the first item in the column, including the current item and turns it into a list"""
    new_lst = []
    for row in range(len(grid)):
        if row == 0:
            new_lst += [[grid[row][col]]]
            continue
        value = grid[row][col] + new_lst[row-1][0]
        new_lst += [[value]]
    return new_lst

def distances_from(grid):
    """calculates the shortest distance to the point (0,0) for each point in a grid"""
    new_grid = []
    new_grid += [accumulate_row_distance(grid[0])]
    col_0 = accumulate_col_distance(grid, 0)
    new_grid += col_0[1:]
    for row in range(len(new_grid)-1):
        for col in range(len(new_grid[0])-1):
            new_grid[row+1] += [min(new_grid[row][col+1], new_grid[row+1][col]) + grid[row+1][col+1]]
    return new_grid


def shortest_path(dists, point):
    """returns the path of the shortest distance from the given point to the point (0,0)"""
    path = []
    row = point[1]
    col = point[0]
    while(True): 
        path += [tuple([col,row])]
        if (row + col) == 0:
            break
        if row == 0:
            col -= 1
            continue
        if col == 0:
            row -= 1
            continue
        if dists[row-1][col] < dists[row][col-1]:
            row -= 1
        else:
            col -= 1
    return path

dists = [
            [1, 6, 13, 14],
            [4, 10, 14, 16],
            [11, 12, 15, 20],
        ]
shortest_path(dists, (3,2))
