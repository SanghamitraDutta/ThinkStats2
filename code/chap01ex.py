"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import pandas as pd
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
    
preg = nsfg.ReadFemPreg()
preg_map = nsfg.MakePregMap(preg)


#fn for counting no. of pregnancies for a given id
preg_count = lambda id: len(preg_map[id])
    
        

preg['pregnum'] = preg['caseid'].map(preg_count)
print(preg['pregnum'][:10])


