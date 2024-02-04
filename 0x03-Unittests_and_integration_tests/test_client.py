#!/usr/bin/env python3
"""UNIT & INTEGRATION TESTS MODULE"""

from client import GithubOrgClient, get_json
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock


class TestGithubOrgClient(TestCase):
    """Tests for the GithubOrgClient class"""
    @parameterized.expand([
        ('google'),
        ('apple'),
    ])
    @mock.patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_org):
        """test that GithubClient.org returns the correct value
        """
        ORG_URL = "https://api.github.com/orgs/"
        test_git_org = GithubOrgClient(mock_org)
        test_resp = test_git_org.org
        # print(mock_org)
        self.assertEqual(test_resp, mock_org.return_value)
        mock_org.assert_called_once()
        mock_org.assert_called_with(f"{ORG_URL}{mock_org}")
        mock_org.assert_any_call(GithubOrgClient.ORG_URL.format(org=mock_org))

    @mock.patch.object(GithubOrgClient, 'org', new_callable=mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ test that GithubOrgClient._public_repos_url
            returns the expected result based on the mocked payload
        """
        test_org = {"repos_url": "mock_url"}
        test_payload = [{"name": "test_repo", "license": {"key": "mit"}}]
        mock_org.return_value = test_org
        test_org = GithubOrgClient(mock_org)
        test_url = test_org._public_repos_url
        self.assertEqual(test_url, mock_org.return_value.get('repos_url'))
        mock_org.assert_called_once()
        # mock_org.assert_any_call(
        # GithubOrgClient.ORG_URL.format(org=mock_org))

    @mock.patch('client.get_json', return_value=[
        {"name": "rep1"}, {"name": "rep2"}
        ])
    def test_public_repos(self, mock_get_json):
        """Unit test for clients"""
        with mock.patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=mock.PropertyMock)\
                as mock_repos_url:
            mock_repos_url.return_value = GithubOrgClient.ORG_URL
            client = GithubOrgClient('org_name')
            repos = client.public_repos()
            self.assertEqual(repos, ['rep1', 'rep2'])
            mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL)
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo_url, key, expected):
        """ test that GithubOrgClient.test_has_license
            returns the expected result based on the mocked result
        """
        response = GithubOrgClient.has_license(repo_url, key)
        self.assertEqual(response, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """ Integration test: fixtures:
        mock code that sends external requests
    """

    @classmethod
    def setUpClass(cls):
        """mock requests.get to return example payloads found in the fixtures
        """

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = mock.patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test GithubOrgClient.public_repos"""
        alx_test_cls = GithubOrgClient("lax")
        self.assertEqual(alx_test_cls.org, self.org_payload)
        self.assertEqual(alx_test_cls.repos_payload, self.repos_payload)
        self.assertEqual(alx_test_cls.public_repos(), self.expected_repos)
        self.assertEqual(alx_test_cls.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ method to test test the public_repos with the argument
            license="apache-2.0" and make sure the result matches the expected
            value from the fixtures
        """
        alx_test_cls = GithubOrgClient("lax")
        self.assertEqual(alx_test_cls.public_repos(), self.expected_repos)
        self.assertEqual(alx_test_cls.public_repos("XLICENSE"), [])
        self.assertEqual(
            alx_test_cls.public_repos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()
