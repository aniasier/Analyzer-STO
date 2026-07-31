import numpy as np
from loader import *
from plotter import *
from routines import *

def main():
    dir = '/home/ania/Documents/Results/STO-sf/ploty/sigma/'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/test/RUN_sigma_1.0/data'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/model1/n0/RUN_n0_trapped_3.0/data'

    # max_iter = 4
    var_tab = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    var_name = 'sigma'
    init_vs_final_size_xy(dir, var_tab, var_name)
    init_vs_final_size_z(dir, var_tab, var_name)
    # check_final(dir)
    # default(dir, max_iter)
    # potential_check(dir, max_iter)

if __name__ == "__main__":
    main()
