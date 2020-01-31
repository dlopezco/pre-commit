#!/usr/bin/env python
import re, sys, os
import subprocess

def main():
    # example:
    # feat(apikey): added the ability to add api key to configuration
    pattern = r'(build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert)(\([\w\-]+\))?:\s.*'
    old, new, branch = sys.stdin.read().split()
    print(old)
    print(new)
    print(branch)
    proc = subprocess.Popen(["git", "rev-list", "--oneline","--first-parent" , "%s..%s" %(old, new)], stdout=subprocess.PIPE)
    commitMessage=str(proc.stdout.readlines()[0])
    print(commitMessage)
    try:
        message = subprocess.check_output(['HEAD']).decode('UTF-8')
    except:
        raise Exception("No message joined for commit")
    print(message)
    m = re.match(pattern, message)
    if m == None: raise Exception("conventional commit validation failed")

if __name__ == "__main__":
    main()