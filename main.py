import numpy as np
from loader import *
from plotter import *
from routines import *

def main():
    dir = '/home/alina/Documents/STO-self_focusing/data'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/test/RUN_sigma_1.0/data'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/model1/n0/RUN_n0_trapped_3.0/data'

    # max_iter = 4

    check_final(dir)
    # default(dir, max_iter)
    # potential_check(dir, max_iter)

if __name__ == "__main__":
    main()