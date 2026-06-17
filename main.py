import numpy as np
from loader import *
from plotter import *

def main():
    dir = '/home/alina/Documents/STO-self_focusing/data'
    num = 1
    df = load_2D_map(f"{dir}/density.dat")
    plot_2D_map(df, f"{dir}/plots/density_before", f"density_before")

    df = load_2D_map(f"{dir}/potential_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_{num}", f"potential_{num}")

    df = load_2D_map(f"{dir}/potential_final_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/potential_final_{num}", f"potential_final_{num}")

    df = load_2D_map(f"{dir}/density3D_{num}.dat")
    plot_2D_map(df, f"{dir}/plots/density_after_{num}",f"density_after_{num}" )

if __name__ == "__main__":
    main()