import numpy as np
from loader import *
from plotter import *

def main():
    dir = '/home/alina/Documents/STO-self_focusing/data'
    df = load_2D_map(f"{dir}/density.dat")
    plot_2D_map(df, f"{dir}/plots/density_before")

    df = load_2D_map(f"{dir}/density3D.dat")
    plot_2D_map(df, f"{dir}/plots/density_after")

if __name__ == "__main__":
    main()