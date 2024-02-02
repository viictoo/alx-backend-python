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


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
