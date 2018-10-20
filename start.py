# -*- coding: utf-8 -*-
"""
Creates a boilerplate file for the euler problem number provided

Usage: python start.py 29
"""

import sys
import re
from urllib2 import urlopen

boilerplate = '''# -*- coding: utf-8 -*-
"""
{text}

https://projecteuler.net/problem={num}
"""

import timer

@timer.many(1)
def main():
    return 1

main()

#
'''

problem_matcher = r'role=\"problem\">([\S\s]*?)</div>'
tag_matches = r'<[\s\S]*?>([\s\S]*?)</[\s\S]*?>'
closed_tag_matches = r'<(.*?)/\s*>'

def get_problem(html):
    matches = re.findall(problem_matcher, html, re.MULTILINE)
    if len(matches) != 1:
        print 'Failed to read problem from html'
        exit(1)
    return matches[0]

def clean(problem_html):
    problem_html = problem_html.replace('<sup>', '^')
    return re.sub(r'<.*?>', '', problem_html).replace('\n\n', '')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Problem number is required'
        exit(1)
    num = int(sys.argv[1])
    resp = urlopen('https://projecteuler.net/problem=%d' % num)
    problem = clean(get_problem(resp.read()))
    with open('python/%03d.py' % num, 'w') as f:
        f.write(boilerplate.replace('{text}', problem).replace('{num}', str(num)))
    print 'Created python/%03d.py' % num