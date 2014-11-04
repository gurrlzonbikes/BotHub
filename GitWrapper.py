__author__ = 'Tual'
import requests
import json
from subprocess import call

class GitWrapper:

    def commitThis(self):
        os = call(['ls', '-l'])