#!/usr/bin/env python3
"""UNIT & INTEGRATION TESTS MODULE FOR UTILS
"""
import unittest
from unittest import TestCase, mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map as accessMap, get_json, memoize


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

    @parameterized.expand([
        ("root", {}, ("a",)),
        ("last child", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         name: str,
                                         nested_map: Mapping,
                                         path: Sequence
                                         ) -> None:
        """tests for access_nested_map function method"""
        with (self.assertRaises(KeyError)):
            accessMap(nested_map, path)


class TestGetJson(TestCase):
    """unittests for the access nested map function

    Args:
        TestCase (class): A class whose instances are single test cases.
    """
    @parameterized.expand([
        ("test_example", "http://example.com", {"payload": True}),
        ("test_holberton", "http://holberton.io", {"payload": False}),
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(self,
                      name: str,
                      url: str,
                      test_response: dict,
                      mock_requests: Any
                      ) -> None:
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
            # self.assertEqual(test_class.a_property(), 42) || returns mock id
            mock_method.assert_called_once()
