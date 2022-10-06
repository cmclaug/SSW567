import unittest
import requests
import json

def gitHubResults(userID):
    x = requests.get("https://api.github.com/users/" + userID + "/repos")
    x = x.json()
    result = ""
    for i in x:
        result = result + "Repo: " + i["name"]
        y = requests.get("https://api.github.com/repos/" + userID + "/" + i["name"] + "/commits")
        y = y.json()
        result = result + " Number of commits: " + str(len(y)) + "\n"
    return result[:-1]

class Test(unittest.TestCase):
    def test_gitHubResults(self):
        self.assertEqual(gitHubResults("richkempinski"), "\nRepo: csp Number of commits: 2\nRepo: hellogitworld Number of commits: 30\nRepo: helloworld Number of commits: 6\nRepo: Mocks Number of commits: 10\nRepo: Project1 Number of commits: 2\nRepo: richkempinski.github.io Number of commits: 9\nRepo: threads-of-life Number of commits: 1\nRepo: try_nbdev Number of commits: 2\nRepo: try_nbdev2 Number of commits: 5")
