import sys
from lxml import etree

def validate(xmlparser, xmlfilename):
    try:
        with open(xmlfilename, 'r') as f:
            etree.fromstring(f.read(), xmlparser) 
        return True
    except:
        print "XML validation error:"
        print sys.exc_info()[0]
        print sys.exc_info()[1]
        #print sys.exc_info()[2]
        return False

#main
if (len(sys.argv) != 3):
    print 'Usage: %s <schema_file (.xsd)> <xml_file>' % sys.argv[0];
    sys.exit(-1);

sSchemaFn = sys.argv[1];
sFn = sys.argv[2];

with open(sSchemaFn, 'r') as f:
    schema_root = etree.XML(f.read())

rSchema = etree.XMLSchema(schema_root)
rXmlParser = etree.XMLParser(schema=rSchema)

if validate(rXmlParser, sFn):
    print "%s CONFORMS_TO %s" % (sFn, sSchemaFn);
else:
    print "%s FAILS_TO_CONFORM_TO %s" % (sFn, sSchemaFn);
