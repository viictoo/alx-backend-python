#!/usr/bin/env python3
""" Complex types - list of floats
    take a list of integers and floats and return their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list([5, 4, 3.14, 666, 0.99])
        returns 679.13 which is a <class 'float'>
    """
    return sum(mxd_lst)
