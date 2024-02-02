#!/usr/bin/env python3
"""
UNIT & INTEGRATION TESTS MODULE
UNIT & INTEGRATION TESTS MODULE
UNIT & INTEGRATION TESTS MODULE
"""
from unittest import TestCase, mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
accessMap = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(TestCase):
    """unittests for the access nested map function

    Args:
        TestCase (class): A class whose instances are single test cases.
    """
    @parameterized.expand([
        ("root", {"a": 1}, ("a",), 1),
        ("children", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("last child", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               name: str,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any
                               ) -> None:
        """tests for access_nested_map method
        """
        self.assertEqual(accessMap(nested_map, path), expected)
