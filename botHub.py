from ApiWrapper import ApiWrapper
import pprint
__author__ = 'Tual'

def forkRepoSafely():
    wrapper = ApiWrapper("gurrlzonbikes", "starcraft666")
    my_reps = wrapper.listOwnRepos()
    random_rep = wrapper.get_hot_repos()
    #print(random_rep['full_name'])
    check = wrapper.checkDoubleRepo(my_reps, random_rep)
    print(check)

if __name__ == '__main__':
    forkRepoSafely()
