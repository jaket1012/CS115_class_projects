

def parse_file(filename):
    myfile = open("Homework\\HW6\\" + filename, "r")
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

    pass

# C:\Users\DYLAN\OneDrive\Desktop\Classes\CS115\Homework\HW6\grids\mini_city.txt # path absolute
# Homework\HW6\grids\mini_city.txt

def accumulate_row_distance(lst):
    new_lst = []
    for item in range(len(lst)):
        if item == 0:
            new_lst += [lst[item]]
            continue
        new_lst += [lst[item] + new_lst[item-1]]
    return new_lst

def accumulate_col_distance(grid, col):
    new_lst = []
    for row in range(len(grid)):
        if row == 0:
            new_lst += [[grid[row][col]]]
            continue
        value = grid[row][col] + new_lst[row-1][0]
        new_lst += [[value]]
    return new_lst

def distances_from(grid):
    new_grid = []
    new_grid += [accumulate_row_distance(grid[0])]
    col_0 = accumulate_col_distance(grid, 0)
    new_grid += col_0[1:]
    for row in range(len(new_grid)-1):
        for col in range(len(new_grid[0])-1):
            new_grid[row+1] += [min(new_grid[row][col+1], new_grid[row+1][col]) + grid[row+1][col+1]]
    return new_grid


def shortest_path(dists, point):
    pass

grid = parse_file("grids/example.txt")
distances_from(grid)