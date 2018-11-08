'''
Generate a .bat file from various inputs, like:
1) Glob-masks, *.dat

The output written to stdout.
'''

import sys, os;
import glob;

##############################################
#main
if (len(sys.argv) != 4):
    print 'Usage: %s "<exe>" "<glob_mask>" "<trailing_params>"' % sys.argv[0];
    print 'Example: %s "foo.exe" "*.dat" "-i -l UPPER"' % sys.argv[0];
    print 'Example: %s "c:\Tools\AMTDICOMEditor\DICOMEditor.exe" "*.dcm" "MachineName RADIMSPC"' % sys.argv[0];
    sys.exit(-1);

sCmd = sys.argv[1];
sGlob = sys.argv[2];
sTrailParam = sys.argv[3];

vFn = glob.glob(sGlob);
vFn.sort();

for sFn in vFn:
    pass;
    #print sFn;
    print '"%s" "%s" %s' % (sCmd, sFn, sTrailParam);
