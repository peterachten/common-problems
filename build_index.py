#!/usr/bin/env python3
import glob
import json
from os.path import basename
import re
import sys

failure = False

def error(msg):
    global failure
    failure = True
    print('\033[0;31mError: ' + msg + '\033[0m')

def extract_keywords(lines):
    keywords = [l[10:-1].split(';') for l in lines if l[:10] == 'Keywords: ']
    keywords = sum(keywords, [])
    keywords = [re.escape(kw.strip()).replace(r'\%', r'.*') for kw in keywords]
    return keywords

def extract_description(lines):
    desc = ''

    reading = False
    for l in lines:
        if l[:3] == '## ':
            break
        if reading:
            desc += l
        if l[:10] == 'Keywords: ':
            reading = True

    return desc.strip()

def extract_solutions(lines):
    sols = []

    reading = False
    for l in lines:
        if l[:-1] == '## Examples':
            break
        if reading:
            if l[:2] == '- ':
                sols.append(l[2:-1])
            elif l[:2] == '  ':
                sols[-1] += ' ' + l[2:-1]
        if l[:-1] == '## Solutions':
            reading = True

    return [sol.strip() for sol in sols]

def extract_examples(lines):
    exs = ['']

    reading = False
    for l in lines:
        if reading:
            if l[:-1] == '---':
                exs.append('')
            else:
                exs[-1] += l
        if l[:-1] == '## Examples':
            reading = True

    return [ex.strip() for ex in exs if ex != '']

def index(fname):
    with open(fname, 'r') as f:
        print('Indexing {}...'.format(fname))
        lines = f.readlines()

        title = lines[0][2:-1]
        keywords = extract_keywords(lines)
        description = extract_description(lines)
        solutions = extract_solutions(lines)
        examples = extract_examples(lines)

        if len(keywords) == 0:
            error('no keywords found')
        if description == '':
            error('no description found')
        if len(solutions) == 0:
            error('no solutions found')
        if len(examples) == 0:
            error('no examples found')

        examples = [ex for ex in examples if ex != 'N/A']

        return {
            'key': basename(fname)[:-3],
            'title': title,
            'keywords': keywords,
            'description': description,
            'solutions': solutions,
            'examples': examples
            }

if __name__ == '__main__':
    problems = []

    for f in glob.glob('*.md'):
        if f != 'README.md':
            problems.append(index(f))

    with open('common-problems.json', 'w') as f:
        f.write(json.dumps(problems))

    if failure:
        sys.exit(1)
