import re
import sys
import glob
import codecs

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s <pattern> <filename>\n" % sys.argv[0])
        sys.exit(1)

    sPattern = sys.argv[1];
    vFnamePattern = sys.argv[2:]

    for sFnamePattern in vFnamePattern:
        for sFn in glob.iglob(sFnamePattern):
            print "---"
            print "Searching file", sFn
            for sLine in codecs.open(sFn, 'r', encoding='utf16'):
                    if re.search(sPattern, sLine):
                        #print "aaa"
                        sLine2 = sLine.rstrip('\r\n')
                        sLineAscii = sLine2.encode('ascii', 'ignore').decode('ascii')
                        print sLineAscii
#
