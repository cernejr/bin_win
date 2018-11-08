'''
Indent/prettify all XML files in a given dir. Performed in-place.
'''
import sys, os, glob;
import xml.dom.minidom

def process_file_dummy(sFn):
    nLineCount = sum(1 for line in open(sFn))
    print nLineCount, sFn;

def process_file(sFn):
    nLineCount = sum(1 for line in open(sFn))

    # Only process one-line or 2-line files
    if (nLineCount > 2):
        return 0;

    #print sFn;
    sXml1 = xml.dom.minidom.parse(sFn)
    sXml2 = sXml1.toprettyxml(indent='  ')
    #print sXml2
    with open(sFn, "w") as f:
        f.write(sXml2)
    return 1;

if __name__=="__main__":
    sDir = '.'

    if (len(sys.argv) != 2):
        print 'Usage: %s <dir_with_xml_files>' % sys.argv[0];
        sys.exit(-1);

    sDir = sys.argv[1];
    sMask = sDir + '/*.xml'
    vFn = glob.glob(sMask);

    nProcessedFileCount = 0;

    for sFn in vFn:
        n = process_file(sFn)
        nProcessedFileCount += n;

    print "Processed %d files." % nProcessedFileCount
