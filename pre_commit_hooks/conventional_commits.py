#!/usr/bin/env python
import re, sys, os
import subprocess

def main():
    # example:
    # feat(apikey): added the ability to add api key to configuration

    pattern = r'(build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert)(\([\w\-]+\))?:\s.*'

    #Get the commit file
    commitMessageFile = open(sys.argv[1]) #The first argument is the file
    commitMessage = commitMessageFile.read().strip()
    print(commitMessage)

    m = re.match(pattern, commitMessage)
    if m == None: raise Exception("conventional commit validation failed")

if __name__ == "__main__":
    main()