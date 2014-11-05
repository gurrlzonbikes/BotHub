from ApiWrapper import ApiWrapper
from getpass import getpass
import pprint
import pdb

pp = pprint.PrettyPrinter(indent=4)

__author__ = 'Tual'

class MeBot:

    def __init__(self):
        credentials_user_name = input("Enter Github username: ")
        credentials_pwd = getpass("Enter Github password: ")
        self.fork_repo_safely(credentials_user_name, credentials_pwd)

    def fork_repo_safely(self, username, password):
        github_wrapper = ApiWrapper(username, password)
        my_reps = github_wrapper.list_own_repos()
        #pdb.set_trace()
        random_rep = github_wrapper.get_hot_repos()
        print(random_rep['full_name'])
        if github_wrapper.checkDoubleRepo(my_reps, random_rep):
            print("Repository already exists")
            self.fork_repo_safely(username, password)

        elif github_wrapper.checkRepoHasForks(random_rep) == False:
            print("Repo has under 1 fork, moving on...")
            self.fork_repo_safely(username, password)

        else:
            #pdb.set_trace()
            github_wrapper.fork_repo(random_rep)
            print(github_wrapper.update_progress(100))




MeBot()

