#!/usr/bin/python
'''
Recursively replace spaces in filenames with underscores
'''

import sys, os, itertools, string

#main, begin
if len(sys.argv) < 2:
    print >> sys.stderr, "usage: %s <dirname>" % os.path.basename(sys.argv[0])
    sys.exit(2)

if not os.path.isdir(sys.argv[1]):
    print >> sys.stderr, sys.argv[1], "not a directory"
    sys.exit(1)

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in itertools.chain(files, dirs):
        old = os.path.join(root, fname)
#        new = os.path.join(root, fname.lower())
        new = string.replace(old, ' ', '_')
        #print old, new, fname
        if not os.path.exists(new):
            print new
            os.rename(old, new)

