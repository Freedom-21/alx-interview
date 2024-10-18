#!/usr/bin/python3
"""
This module contains a function that determines
if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists,
        where each sublist contains keys for other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
