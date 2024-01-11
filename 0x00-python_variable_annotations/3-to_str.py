#!/usr/bin/env python3
"""Basic annotations - to string
"""


def to_str(n: float) -> str:
    """type-annotated function to_str that takes
        a float n as argument and returns the string
        representation of the float

    Args:
        n (float): argument

    Returns:
        str: to_str(3.14) returns 3.14, which is a <class 'str'
    """
    return (str(n))
