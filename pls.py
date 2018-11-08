#!/usr/bin/env python

import os.path
import sys, glob

def find_files001(pattern, path):
    s = os.path.join(path, pattern)
    #print s
    sza = glob.glob(s)
    sza2 = sorted(sza)
    #print sza2
    return sza2    

#main
if len(sys.argv) < 2:
    sys.exit(-1)
    
sz = sys.argv[1]
#print sz
sza = find_files001(sz, ".")
for s2 in sza:
    #print s2
    print os.path.abspath(s2)
