import numpy as np
from loader import *
from plotter import *
from routines import *

def main():
    dir = '/home/alina/Documents/STO-self_focusing/data'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    dir = '/home/alina/Documents/Results/STO-self-focusing/test_effective_mass/RUN_m1_2.0/data'
    dir = '/home/ania/Documents/Results/STO-sf/RUN_m1_0.28/data'

    max_iter = 8

    default(dir, max_iter)

if __name__ == "__main__":
    main()