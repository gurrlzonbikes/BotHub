from ApiWrapper import ApiWrapper
import pprint
import pdb

__author__ = 'Tual'

def forkRepoSafely():
    wrapper = ApiWrapper("gurrlzonbikes", "starcraft666")
    my_reps = wrapper.listOwnRepos()
    random_rep = wrapper.get_hot_repos()
    print(random_rep['full_name'])
    if wrapper.checkDoubleRepo(my_reps, random_rep):
        print("Repository already exists")
    else:
        #pdb.set_trace()
        wrapper.forkRepo(random_rep)
        print(wrapper.update_progress(100))

if __name__ == '__main__':
    forkRepoSafely()
