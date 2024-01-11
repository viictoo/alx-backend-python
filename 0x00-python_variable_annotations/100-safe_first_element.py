#!/usr/bin/env python3
""" Duck typing - first element of a sequence  """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """fn with correct duck-typed annotations

    Args:
        lst (Sequence[Any]): Types of the elements of the input are not known

    Returns:
        Union[Any, None]: list or none if not a list
    """
    if lst:
        return lst[0]
    else:
        return None
