#!/usr/bin/python3
"""UNIT & INTEGRATION TESTS MODULE"""

from client import GithubOrgClient, get_json
from parameterized import parameterized
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
        # mock_org.assert_any_call(GithubOrgClient.ORG_URL.format(org=mock_org))
