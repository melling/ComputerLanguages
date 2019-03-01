#!/usr/bin/env python3

"""
Simple script to convert .org url lines to .md urls

+ [[http://www.h4labs.com][h4labs]]
to
+ [h4labs](http://www.h4labs.com)

If the line doesn't match, simply print the line.

bin/org_url2md.py haskell.md

"""
import os
import sys
import re

prog = re.compile(r"\+ \[\[(.*?)\]\[(.*?)\]\]")


def convert2md(line):
	str = line.strip()
	m = prog.match(str)

	if m:
		n = len(m.groups())
		#print("n={}".format(len(m.groups())))
		if n == 2:
			print("+ [{}]({})".format(m.group(2), m.group(1)))
			return

	print("{}".format(str))

	
def org2md(fname):
    with open(fname) as fp:
        line = fp.readline()
        while line:
            convert2md(line)
            # print("{}".format(line), end="")
            line = fp.readline()


filepath = sys.argv[1]

if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

org2md(filepath)

