import sys
from tests import generate_output

if __name__ == '__main__':
    verbose = False
    if '-v' in sys.argv or '--verbose' in sys.argv:
        verbose=True
        
    generate_output(verbose)
    