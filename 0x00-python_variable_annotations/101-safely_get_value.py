#!/usr/bin/env python3
""" More involved type annotations
    Given the parameters and the return values,
    add type annotations to the function
"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """_summary_

    Args:
        dct (Mapping): args
        key (Any): args
        default (Union[T, None], optional): TypeVar. Defaults to None.

    Returns:
        Union[Any, T]: default
    """
    if key in dct:
        return dct[key]
    else:
        return default
