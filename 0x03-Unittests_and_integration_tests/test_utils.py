#!/usr/bin/env python3
"""UNIT & INTEGRATION TESTS MODULE
"""
from unittest import TestCase, mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
accessMap = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    # unittest does not support test decorators,
    # only tests created with @parameterized.expand will be executed
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method returns correct output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


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
