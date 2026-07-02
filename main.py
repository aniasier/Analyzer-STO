import numpy as np
from loader import *
from plotter import *

def main():
    dir = '/home/alina/Documents/STO-self_focusing/data'
    # dir700 = '/home/alina/Documents/STO-self_focusing/data/700'
    dir = '/home/alina/Documents/Results/STO-self-focusing/test_effective_mass/RUN_m1_2.0/data'
    # df100 = load_file(f"{dir100}/electric_field_trapped.dat")
    # df700 = load_file(f"{dir700}/electric_field_trapped.dat")

    # plt.plot(df100['z'], df100['fun'], label="100")
    # plt.plot(df700['z'], df700['fun'], label="700")
    # plt.legend()
    # plt.show()
    max_iter= 8

    file_list = load_iter_make_list(f"{dir}/density_final_crossection", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssections")
    file_list = load_iter_make_list(f"{dir}/density_final_crossection_x", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssections_x")
    file_list = load_iter_make_list(f"{dir}/density_final_crossection_y", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssections_y")

    # import sys
    # sys.exit()
    num = max_iter
    
    df = load_2D_map(f"{dir}/potential_nocharge_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_nocharge_{num}", f"potential_no_charge")

    df = load_2D_map(f"{dir}/potential_plus_z_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_plus_z_{num}", f"potential_plus_z")

    # df = load_2D_map(f"{dir}/potential_eps0{num}.dat")
    # plot_2D_map(df, f"{dir}/plots/potential_eps0{num}", f"potential_eps0")

    df = load_2D_map(f"{dir}/density.dat")
    plot_2D_map(df, f"{dir}/plots/density_before", f"density_before")

    df = load_2D_map(f"{dir}/potential_final_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_final_{num}", f"potential_final_{num}")

    df = load_2D_map(f"{dir}/density3D_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/density_after_{num}",f"density_after_{num}" )

    df = load_2D_map(f"{dir}/density_final_slice_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/density_final_slice{num}",f"density_final_slice_{num}" )

if __name__ == "__main__":
    main()