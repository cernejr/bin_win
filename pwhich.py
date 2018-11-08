from __future__ import print_function

import sys
import os
import os.path
import stat

def usage():
    sys.stderr.write("Usage: python pwhich.py name\n") 
    sys.stderr.write("or: pwhich.py name\n") 

def which(name):
    found = 0 
    for path in os.getenv("PATH").split(os.path.pathsep):
        full_path = os.path.join(path, name)
        if os.path.exists(full_path):
            """
            if os.stat(full_path).st_mode & stat.S_IXUSR:
                found = 1
                print(full_path)
            """
            found = 1
            s2 = full_path.replace("\\", "/");
            print(s2)
    # Return a UNIX-style exit code so it can be checked by calling scripts.
    # Programming shortcut to toggle the value of found: 1 => 0, 0 => 1.
    sys.exit(1 - found)

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    which(sys.argv[1])

if "__main__" == __name__:
        main()
