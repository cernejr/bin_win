import re
import sys
import glob

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s <pattern> <filename>\n" % sys.argv[0])
        sys.exit(1)

    sPattern = sys.argv[1];
    vFname = sys.argv[2:]

    for sFname in vFname:
        for file in glob.iglob(sFname):
            for line in open(file, 'r'):
                    if re.search(sPattern, line):
                            print line,
#
