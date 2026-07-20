from loader import *
from plotter import *


def default(dir, max_iter):
    file_list = load_iter_make_list(f"{dir}/density_final_crossection", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssection_z")
    file_list = load_iter_make_list(f"{dir}/density_final_crossection_x", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssections_x")
    file_list = load_iter_make_list(f"{dir}/density_final_crossection_y", max_iter)
    crossection_in_iters(file_list, max_iter, f"{dir}/plots/crosssections_y")
    
    df = load_2D_map(f"{dir}/density.dat")
    plot_2D_map(df, f"{dir}/plots/density_before", f"density_before")

    df = load_2D_map(f"{dir}/density3D_{max_iter}.dat")
    plot_2D_map(df, f"{dir}/plots/density_after_{max_iter}",f"density_after_{max_iter}" )

def potential_check(dir, max_iter):
    df = load_2D_map(f"{dir}/potential_nocharge_{max_iter}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_nocharge_{max_iter}", f"potential_no_charge")

    df = load_2D_map(f"{dir}/potential_plus_z_{max_iter}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_plus_z_{max_iter}", f"potential_plus_z")

    # df = load_2D_map(f"{dir}/potential_eps0{max_iter}.dat")
    # plot_2D_map(df, f"{dir}/plots/potential_eps0{max_iter}", f"potential_eps0")

    df = load_2D_map(f"{dir}/potential_final_{max_iter}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_final_{max_iter}", f"potential_final_{max_iter}")

def check_final(dir):
    file_list = []
    file_list.append(load_file(f"{dir}/density_init_crossection.dat"))
    file_list.append(load_file(f"{dir}/density_final_crossection.dat"))
    crossection_in_iters(file_list, 2, f"{dir}/plots/crosssection_z")

    file_list = []
    file_list.append(load_file(f"{dir}/density_init_crossection_x.dat"))
    file_list.append(load_file(f"{dir}/density_final_crossection_x.dat"))
    crossection_in_iters(file_list, 2, f"{dir}/plots/crosssection_x")

    file_list = []
    file_list.append(load_file(f"{dir}/density_init_crossection_y.dat"))
    file_list.append(load_file(f"{dir}/density_final_crossection_y.dat"))
    crossection_in_iters(file_list, 2, f"{dir}/plots/crosssection_y")

    df = load_2D_map(f"{dir}/density_init.dat")
    plot_2D_map(df, f"{dir}/plots/density_before", f"density_before")

    df = load_2D_map(f"{dir}/density_final.dat")
    plot_2D_map(df, f"{dir}/plots/density_after",f"density_after" )
