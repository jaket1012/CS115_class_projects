import random
# === CS 115 Homework 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:"I pledge my honor that I have abided by the Stevens Honor System."
#
# === CS 115 Homework 5 ===

class Item:
    """
    Fill in description here
    """
    def __init__(self, name, damage_points, regeneration_points, damage_type, is_consumable):
        self.name = name
        self.damage_points = damage_points
        self.damage_type = damage_type
        self.regeneration_points = regeneration_points
        self.is_consumable = is_consumable

    def __str__(self):
        return "Name: " + self.name + ", Type: " + self.damage_type + ", Damage: " + str(self.damage_points) + ", Regeneration: " + str(self.regeneration_points) + ", Consumable: " + str(self.is_consumable)

    def __lt__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return self.damage_points < other.damage_points

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __repr__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return str(self)

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

class Move:
    """
    Represents an action a character takes in a turn.
    """

    def __init__(self, other_character, item):
        self.other_character = other_character
        self.item = item

    def __str__(self):
        """ pretty prints Move. Do not change, but you can use as an example """
        return "Move: " + "\r\n" + "    Item: " + str(self.item) + "\r\n" + "    Target character: " + str(self.other_character)

basic_weapon = Item("rusty axe", 1, 0, "physical", False)

class Character:
    def __init__(self, name, max_health_points):
        self.name: str = name
        self.health_points: int = max_health_points
        self.inventory: dict = {basic_weapon: 1}

    def __str__(self):
        return "Name: " + self.name + ", hp: " + str(self.health_points)

    def __lt__(self, other):
        return self.health_points < other.health_points

    def transfer_loot(self, loot):
        """moves all the items in loot into self.inventory"""
        for item in loot:
            self.inventory[item] += loot[item]
            loot[item] -= loot[item]
    
    def perform_move(self, move):
        """calls a charater to perform a given move by using the given item to take hp away from the character in move and regerating health with the items regeneration points and consuming the item if it is consumable"""
        if move.item not in self.inventory:
            return
        move.other_character.health_points -= move.item.damage_points
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable:
            self.inventory[move.item] -= 1

    def get_next_move(self, other_characters):
        """Returns a Move targeting the character with lowest HP using strongest item."""
        character_to_attack = min(other_characters, key = lambda other_character: other_character.health_points)
        attack_item = max(self.inventory, key = lambda item: item.damage_points)
        next_move =  Move(character_to_attack, attack_item)
        return next_move

    # TODO Add other methods here.

shock_baton = Item("shock baton", 1, 0, "electrical", False)
class Robot(Character):
    def __init__(self, name, max_health_points):
        self.name: str = name
        self.health_points: int = max_health_points
        self.inventory: dict = {basic_weapon: 1, shock_baton: 1}
    
    def get_next_move(other_characters):
        """returns a move item attacking the first character and chooses the highest damage electrical item."""
        character_to_attack = other_characters[0]
        def is_electrical(item):
            if item.damage_type == "electrical":
                return True
            else:
                return False
        electrical_items = filter(is_electrical, character_to_attack.inventory)
        attack_item = max(electrical_items, key = lambda item: item.damage_points)
        next_move = Move(character_to_attack, attack_item)
        return next_move
    
    def perform_move(self, move):
        """calls a charater to perform a given move by using the given item to take hp away from the character in move and regerating health with the items regeneration points and consuming the item if it is consumable"""
        if move.item not in self.inventory:
            return
        if move.item.damage_type == "electrical":
            move.other_character.health_points -= move.item.damage_points
        move.other_character.health_points -= move.item.damage_points
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable:
            self.inventory[move.item] -= 1

brain_grenade = Item("brain grenade", 5, 0, "viral", True)
class Zombie(Character):
    def __init__(self, name, max_health_points):
        self.name: str = name
        self.health_points: int = max_health_points
        self.inventory: dict = {basic_weapon: 1, brain_grenade: 3}
    
    def get_next_move(self, other_characters):
        """returns a move item attacking the first character and chooses the highest damage viral item."""
        character_to_attack = other_characters[0]
        attack_item = max(self.inventory, key = lambda item: item.damage_points)
        next_move = Move(character_to_attack, attack_item)
        return next_move
    
    def perform_move(self, move):
        """calls a charater to perform a given move by using the given item to take hp away from the character in move and regerating health with the items regeneration points and consuming the item if it is consumable"""
        if move.item not in self.inventory:
            return
        if move.item.damage_type == "viral":
            move.other_character.health_points -= move.item.damage_points
        move.other_character.health_points -= move.item.damage_points
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable:
            self.inventory[move.item] -= 1

class PlayableCharacter(Character):
    def get_user_input(self, other_characters):
        print("Your Inventory:")
        for item in self.inventory:
            print(str(item) + ", Amount: " + str(self.inventory[item]))
        print("Enemies:")
        enemy_num = 0
        for character in other_characters:
            print(str(enemy_num) + ") " + str(character))
            enemy_num += 1
        user_item = get_inventory_item_from_item_name(input("What item do you want to use: "), self.inventory)
        enemy_to_attack = int(input("Which enemy do you want to attack: "))
        return Move(other_characters[enemy_to_attack], user_item)
    
    def get_next_move(self, other_characters):
        """returns a move item attacking the first character and chooses the highest damage viral item."""
        next_move = self.get_user_input(other_characters)
        return next_move


def spawn_enemies():
    """
    returns enemies based on what has already been implemented

    change this to include any characters you have implemented!
    """
    cubebot_1 = Character("little cubebot", 1)
    cubebot_2 = Character("armor cube", 2)
    return [cubebot_1, cubebot_2]

def standard_battle(main_character, enemies, enemy_that_will_attack):
    """
    Executes one round of combat between the player and a chosen enemy.

    Steps:
    1. The main_character selects a move using get_next_move(enemies).
    2. The main_character applies that move to its chosen target.
    3. If the target's health points reach 0, the main_character transfers
       all items from that target's inventory.
    4. Otherwise, enemy_that_will_attack selects a move using
       get_next_move([main_character]) and applies it.
    5. If the main_character's health points reach 0, the attacking enemy
       transfers all items from the main_character's inventory.
    """
    if main_character.health_points > 0 and min(enemies, key = lambda enemy: enemy.health_points).health_points > 0:
        main_character_move = main_character.get_next_move(enemies)
        main_character.perform_move(main_character_move)
        if main_character_move.other_character.health_points <= 0:
            main_character.transfer_loot(main_character_move.other_character.inventory)
        enemy_move = enemy_that_will_attack.get_next_move([main_character])
        enemy_that_will_attack.perform_move(enemy_move)
        if main_character.health_points < 0:
            enemy_that_will_attack.transfer_loot(main_character.inventory)


def main_game_loop():
    """
    Do not change. If you would like a different game loop, implement
    one and call it custom_main_game_loop
    """
    main_character = PlayableCharacter("player", 15)
    enemies = spawn_enemies()
    while True:
        print("Main character info: " + str(main_character))
        enemies = [e for e in enemies if e.health_points > 0]
        if not enemies:
            print("You win!")
            break

        enemy = random.choice(enemies)
        standard_battle(main_character, enemies, enemy)
        print(f"Your stats: {main_character}")

        if main_character.health_points <= 0:
            print("You were defeated!")
            break

def get_inventory_item_from_item_name(item_name, inventory):
    """
    Helper function that might make get_next_move for PlayableCharacter easier
    Returns the Item object from inventory (dict with Item keys)
    whose name matches item_name, or None if not found.
    Assumes there will be just one matching item_name in the
    inventory, or will just match the first
    """
    name_matches = filter(lambda item: item.name == item_name, map(lambda i: i, inventory))
    return next(name_matches, None)

my_char = Character("Mark", 100)
print(my_char)
medkit = Item("Medkit", 0, 25, "Healing", True)
print(medkit)


if __name__ == "__main__":
     # Change any code below to test or run your code
    #other_characters = spawn_enemies()
    #me = PlayableCharacter("alex", 5) #example test code
    #next_move = me.get_next_move(other_characters)
    #print(next_move)
    main_game_loop() # uncomment this to start a game with the staff framework