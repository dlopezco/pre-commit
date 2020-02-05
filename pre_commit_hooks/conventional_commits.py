#!/usr/bin/env python
import re, sys, os

def main():
    # example:
    # feat(apikey): added the ability to add api key to configuration
    pattern = r'(build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert)(\([\w\-]+\))?:\s.*'
    filename = sys.argv[1]
    print(filename)
    ss = open(filename, 'r').read()
    print(ss)
    m = re.match(pattern, ss)
    if m == None: raise Exception("conventional commit validation failed")

if __name__ == "__main__":
    main()