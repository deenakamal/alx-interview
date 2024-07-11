#!/usr/bin/python3
"""
Defines the function min_operations.

This function calculates the minimum number of operations needed to
achieve exactly 'n' characters in the file, starting with 1 character.
"""


def min_operations(target_characters):
    """
    Calculates the fewest number of operations needed
    to achieve exactly 'target_characters'
    characters in the file, starting with 1 character.
    
    Args:
    - target_characters (int): The desired number of characters.

    Returns:
    - int: The minimum number of operations required.
    """
    if target_characters <= 1:
        return 0

    operations_count = 0
    copied_characters = 0
    current_characters = 1

    while current_characters < target_characters:
        if target_characters % current_characters == 0:
            operations_count += 1
            copied_characters = current_characters

        operations_count += 1
        current_characters += copied_characters

    return operations_count
