#!/usr/bin/env python3
"""UNIT & INTEGRATION TESTS MODULE FOR UTILS
"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """unittests for the access nested map function

    Args:
        TestCase (class): A class whose instances are single test cases.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """tests for access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        """tests for access_nested_map function method"""
        with (self.assertRaises(KeyError)):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """unittests for the access nested map function

    Args:
        TestCase (class): A class whose instances are single test cases.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(
            self, url: str, test_response: dict, mock_requests: Any) -> None:
        """assert that the get json method calls the url presented"""
        mock_requests.return_value.json.return_value = test_response
        self.assertEqual(get_json(url), test_response)
        mock_requests.assert_called_once_with(url)


class TestMemoize(TestCase):
    """unittests for the memoize function

    Args:
        TestCase (class): A class whose functions are single test cases
    """

    def test_memoize(self):
        """test method for  utils.memoize method
        """
        class TestClass:
            """ test class with 2 methods"""

            def a_method(self) -> int:
                """this method cachreturns 42"""
                return 42

            @memoize
            def a_property(self) -> Any:
                """method with a cached result"""
                return self.a_method()

        with mock.patch.object(TestClass, "a_method") as mock_method:
            test_class = TestClass()
            for _ in range(7):
                test_class.a_property
            # self.assertEqual(test_class.a_property(), 42)|returns mock id
            mock_method.assert_called_once()
