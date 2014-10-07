from ApiWrapper import ApiWrapper
import pprint
import pdb

__author__ = 'Tual'

def forkRepoSafely():
    github_wrapper = ApiWrapper(<username>, <password>)
    my_reps = github_wrapper.listOwnRepos()
    random_rep = github_wrapper.get_hot_repos()
    print(random_rep['full_name'])
    if github_wrapper.checkDoubleRepo(my_reps, random_rep):
        print("Repository already exists")
    else:
        #pdb.set_trace()
        github_wrapper.forkRepo(random_rep)
        print(github_wrapper.update_progress(100))


if __name__ == '__main__':
    forkRepoSafely()