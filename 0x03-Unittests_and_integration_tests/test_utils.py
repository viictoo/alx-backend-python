#!/usr/bin/env python3
"""
Test suite for utils.py
"""

import unittest
from unittest.mock import patch
from typing import Mapping, Sequence, Any

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


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
