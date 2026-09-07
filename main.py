import numpy as np
from loader import *
from plotter import *
from routines import *

def main():
    dir = '/home/alina/Documents/Results/STO-self-focusing/kp/test/RUN_z0_indx_60/data'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/n0'
    dir = '/home/ania/Documents/Results/STO-sf/wyniki/test/sigma/m05'
    # dir = '/home/alina/Documents/STO-self_focusing/data'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/test/RUN_sigma_1.0/data'
    # dir = '/home/alina/Documents/Results/STO-self-focusing/model1/n0/RUN_n0_trapped_3.0/data'

    # folders = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    # check_epsilon(dir, folders)

    # max_iter = 3
    var_tab = [1.,1.55, 2.1, 2.65, 3.2, 3.75, 4.3, 4.85, 5.4, 5.95, 6.5, 7.05, 7.6, 8.15, 8.7, 9.25, 9.8, 10.35, 10.9, 11.45, 12]
    # var_tab = [0.2 , 0.23, 0.26, 0.29, 0.32, 0.35, 0.38, 0.41, 0.44, 0.47, 0.5 , 0.53, 0.56, 0.59, 0.62, 0.65, 0.68, 0.71, 0.74, 0.77, 0.8]
    # var_tab = [1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8, 5.]
    var_name = 'sigma'
    init_vs_final_size_xy(dir, var_tab, var_name)
    # init_vs_final_size_z(dir, var_tab, var_name)
    # check_final(dir)
    # default(dir, max_iter)
    # full_checking(dir, max_iter)
    # potential_check(dir, max_iter)
    # for i in range(1,10):
    #     df = load_2D_map(f"{dir}/density_xy_{i}.dat")
    #     plot_2D_map(df, f"{dir}/plots/density_xy_{i}", f"iter {i} density (xy)")

if __name__ == "__main__":
    main()
