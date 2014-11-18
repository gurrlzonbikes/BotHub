__author__ = 'Tual'
import subprocess

class repoManagement:

    def clone_repo(self, repo_url):
        #subprocess.call('cd ../', shell=True)
        #subprocess.call(['git clone '+repo_url], shell=True)
        p = subprocess.Popen(['git clone '+repo_url], cwd='/Users/Tual/PycharmProjects', shell=True)
        p.wait()
