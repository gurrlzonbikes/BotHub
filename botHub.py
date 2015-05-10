from ApiWrapper import ApiWrapper
from RepoManagement import repoManagement
from getpass import getpass
import pprint
import pdb

pp = pprint.PrettyPrinter(indent=4)

__author__ = 'Tual'

class MeBot:

    def __init__(self):
        credentials_user_name = input("Enter Github username: ")
        credentials_pwd = getpass("Enter Github password: ")
        repo_name = self.fork_repo_safely(credentials_user_name, credentials_pwd)



    def fork_repo_safely(self, username, password):
        github_wrapper = ApiWrapper(username, password)
        os_management = repoManagement()
        my_reps = github_wrapper.list_own_repos()
        random_rep = github_wrapper.get_hot_repos()
        print(random_rep['full_name'])
        if github_wrapper.check_double_repo(my_reps, random_rep):
            print("Repository already exists")
            self.fork_repo_safely(username, password)

        else:
            github_wrapper.fork_repo(random_rep)
            print(github_wrapper.update_progress(100))
            clone_url = github_wrapper.clone_it(random_rep)
            os_management.clone_repo(clone_url)
            random_py = os_management.select_random_py_file(random_rep['full_name'])
            os_management.insert_random_in_file(random_py)
            os_management.get_comment_strings()
            return random_rep['full_name']


if __name__ == "main":
    MeBot()

