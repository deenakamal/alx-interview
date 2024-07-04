#!/usr/bin/python3
"""canUnlockAll method"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    length = len(boxes)
    unlocked = [0]
    keys = []
    keys.extend(boxes[0])

    while keys:
        key = keys.pop()

        if key not in unlocked and key < length:
            keys.extend(boxes[key])
            unlocked.append(key)

    return len(unlocked) == length
