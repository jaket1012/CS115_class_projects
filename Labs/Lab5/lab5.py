# === CS 115 Lab 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 5 ===
def coin_change(coins, total):
    """takes in a tuple of coins and a target value and returns the least
    amount of coins needed to reach the target value."""
    if total==0:
        return 0
    if len(coins) == 0 or total < 0:
        return float('inf')
    if coins[0] <= total:
        use_it = 1 + coin_change(coins, total - coins[0])
        lose_it = coin_change(coins[1:], total)
        if lose_it == 0:
            return use_it
        return min(use_it,lose_it)
    else:
        return coin_change(coins[1:], total)
