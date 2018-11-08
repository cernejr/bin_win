'''
Execute a command on each file listed in the input file.
Simulate the @list functionality of some command line utilities.
'''
import sys,os;
import subprocess;

def execute_command(sCmd, sFn):
    pass;
    print '%s %s' % (sCmd, sFn);
    v = [sCmd, sFn];
    subprocess.call(v);

if __name__=="__main__":
    pass;
    if (len(sys.argv) != 3):
        print 'Usage: %s <exe> <file_w_list_of_input_files>' % sys.argv[0];
        sys.exit(-1);

    sCmd = sys.argv[1];
    sListFn = sys.argv[2];
    nTot = 0;

    with open(sListFn, 'r') as f:
        for sFn0 in f:
            sFn = sFn0.strip();
            execute_command(sCmd, sFn);
    pass;
