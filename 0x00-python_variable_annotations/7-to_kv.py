#!/usr/bin/env python3
""" Complex types - string and int/float to tuple
    type-annotated fn that takes a string and an
    int OR float as arguments and returns a tuple where:
    The first element of the tuple is the string k.
    The second element is the square of the int/float annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ print(to_kv.__annotations__)
        {'k': <class 'str'>, 'v': typing.Union[int, float],
        'return': typing.Tuple[str, float]}

    Args:
        k (str): string
        v (Union[int, float]): float

    Returns:
        Tuple[str, float]: square of the int/float annotated as a float.
    """
    return (k, v ** 2)
