import numpy as np
from loader import *
from plotter import *
from routines import *

def main():
    # dir = '/home/alina/Documents/Results/STO-self-focusing/sigma-m028/RUN_sigma_10.0/data'
    dir = '/home/alina/Documents/Results/STO-self-focusing/n0'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/n0-m08/RUN_sigma_5.0/data'
    dir = '/home/alina/Documents/STO-self_focusing/data'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/test/RUN_sigma_1.0/data'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/model1/n0/RUN_n0_trapped_3.0/data'

    # folders = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    # check_epsilon(dir, folders)

    max_iter = 11
    # var_tab = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    # var_name = 'n0_trapped'
    # init_vs_final_size_xy(dir, var_tab, var_name)
    # init_vs_final_size_z(dir, var_tab, var_name)
    # check_final(dir)
    # default(dir, max_iter)
    full_checking(dir, max_iter)
    # potential_check(dir, max_iter)
    # for i in range(1,10):
    #     df = load_2D_map(f"{dir}/density_xy_{i}.dat")
    #     plot_2D_map(df, f"{dir}/plots/density_xy_{i}", f"iter {i} density (xy)")

if __name__ == "__main__":
    main()
