# === CS 115 Lab 11 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 11 ===

class Item:
    """
    Constructs an Instance of item with the following attributes
    name: name of the item
    damage_points: how much to reduce enemy HP during an attack
    regeneration_points: healing points to apply to a character if this item is used
    damage_type: type of damage. Can be "viral" "physical" or "electrical"
    is_consumable: true if the item can only be used once
    """
    def __init__(self, name, damage_points, regeneration_points, damage_type, is_consumable):
        self.name = name 
        self.damage_points = damage_points
        self.regeneration_points = regeneration_points
        self.damage_type = damage_type
        self.is_consumable = is_consumable

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

def create_healer_inventory():
    """
    creates an inventory of items for a healer character

    Do not read entire function!!!! Use stack trace and
    the debugger to isolate any errors
    """
    inventory = {
        Item("bandage", 0, 5, "physical", True): 1,
        Item("small_potion", 0, 8, "viral", True) : 3,
        Item("herb", 0, 3, "physical", True): 5,
        Item("antidote", 0, 7, "viral", True):2,
        Item("mega_potion", 0, 20, "viral", True):4,
        Item("revive_leaf", 0, 15, "electrical", True):0, 
        Item("healing_crystal", 0, 30, "physical", False):1,
        Item("ointment", 0, 4, "physical", True):1,
        Item("ginger", 0, 10, "physical", True):1,
        Item("nano_patch", 0, 6, "electrical", True):3,
        Item("bio_gel", 0, 9, "viral", True):5,
        Item("hydration_vial", 0, 12, "physical", True):3,
        Item("regen_orb", 0, 25, "electrical", False):2,
        Item("soothing_salve", 0, 11, "physical", True):1,
        Item("mending_scroll", 0, 14, "viral", True):4,
    }

    return inventory


def compute_total_regeneration_points_in_inventory(inventory):
    """
    Computes the total regeneration points for all Items in the inventory.
    """
    total = 0
    for item in inventory:
        item_quantity = inventory[item]
        total += item_quantity * item.regeneration_points
    return total

###### The rest of the functions are for loop practice, the second part ######

def num_halves_until_one(n):
    amt = 0
    while(n != 1):
        n = n//2
        amt += 1
    return amt


def accumulate_costs(lst):
    new_lst = []
    for item in range(len(lst)):
        if item == 0:
            new_lst += [lst[item]]
            continue
        new_lst += [lst[item] + new_lst[item-1]]
    return new_lst

def accumulate_col_costs(grid, col):
    new_lst = []
    for row in range(len(grid)):
        if row == 0:
            new_lst += [grid[row][col]]
            continue
        new_lst += [grid[row][col] + new_lst[row-1]]
    return new_lst
        
def get_unique_values(grid):
    unique_values = []
    for row in grid:
        for column in range(len(row)):
            if row[column] not in unique_values:
                unique_values += [row[column]]
    return unique_values

def count_shared_values(gridX, gridY):
    gridX_unique_values = get_unique_values(gridX)
    gridY_unique_values = get_unique_values(gridY)
    shared_values = []
    for value in gridX_unique_values:
        if value in gridY_unique_values:
            shared_values += [value]
    return len(shared_values)

if __name__ == "__main__":
     pass
     # Uncomment the code below to reproduce the bug
     #inventory = create_healer_inventory()
     #total_regeneration_points = compute_total_regeneration_points_in_inventory(inventory)
     #print(total_regeneration_points)
     



