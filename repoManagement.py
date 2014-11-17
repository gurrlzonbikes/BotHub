__author__ = 'Tual'
import subprocess

class repoManagement:

    def clone_repo(self, repo_url):
        subprocess.call('cd ../', shell=True)
        subprocess.call(['git clone '+repo_url], shell=True)
