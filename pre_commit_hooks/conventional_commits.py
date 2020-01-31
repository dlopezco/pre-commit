#!/usr/bin/env python
import re, sys, os
import subprocess
import humanhash

def main():
    # example:
    # feat(apikey): added the ability to add api key to configuration
    pattern = r'(build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert)(\([\w\-]+\))?:\s.*'
    try:
        message = humanhash.humanize(subprocess.check_output(['HEAD']))
    except:
        raise Exception("No message joined for commit")
    m = re.match(pattern, message)
    if m == None: raise Exception("conventional commit validation failed")

if __name__ == "__main__":
    main()