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


def get_size(file):
    """Return the 90% width of a 1D profile from a loaded file or dataframe."""
    try:
        if isinstance(file, str):
            data = load_file(file)
        else:
            data = file

        z = np.asarray(data["z"], dtype=float)
        rho = np.asarray(data["fun"], dtype=float)

        if z.size == 0 or rho.size == 0 or z.size != rho.size:
            return float("nan")

        cdf = np.cumsum(rho)
        total = cdf[-1]
        if total == 0:
            return float("nan")

        cdf = cdf / total
        z05 = z[np.searchsorted(cdf, 0.05)]
        z95 = z[np.searchsorted(cdf, 0.95)]
        return float(z95 - z05)
    except Exception:
        return float("nan")

def init_vs_final_size_xy(dir, var_tab, var_name):
    size_list_init = []
    size_list_final = []
    for iter in var_tab:
        file_init = load_file(f"{dir}/RUN_{var_name}_{iter}/data/density_init_crossection_x.dat")
        size_list_init.append(get_size(file_init))
        file_final = load_file(f"{dir}/RUN_{var_name}_{iter}/data/density_final_crossection_x.dat")
        size_list_final.append(get_size(file_final))

    plt.plot(var_tab, size_list_init, '.-', color='red', lw=0.8, ms=5, label='initial')
    plt.plot(var_tab, size_list_final, '.-', color='blue', lw=0.8, ms=5, label='final')
    # plt.plot(var_tab, size_list_init, '-o', lw=1.5, ms=5,
    #      color='tab:red', label='Initial')

    # plt.plot(var_tab, size_list_final, '-o', lw=1.5, ms=5,
    #         color='tab:blue', label='final')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend(frameon=False)
    if var_name=='m1':
        plt.xlabel('$m_{eff}$')
    elif var_name=="n0_trapped":
        plt.xlabel('$n_0$ ($10^{13}$ cm$^{-2}$)')
    elif var_name=="sigma":
            plt.xlabel('$\sigma$ (nm)')
    plt.ylabel('size (nm)')
    plt.tight_layout()
    plots_dir = os.path.join(dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    output_path = os.path.join(plots_dir, f"size_comparison_{var_name}_xy.png")
    plt.savefig(output_path, dpi=300)
    plt.show()

def init_vs_final_size_z(dir, var_tab, var_name):
    size_list_init = []
    size_list_final = []
    for iter in var_tab:
        file_init = load_file(f"{dir}/RUN_{var_name}_{iter}/data/density_init_crossection.dat")
        size_list_init.append(get_size(file_init))
        file_final = load_file(f"{dir}/RUN_{var_name}_{iter}/data/density_final_crossection.dat")
        size_list_final.append(get_size(file_final))

    plt.plot(var_tab, size_list_init, '.-', color='red', lw=0.8, ms=5, label='initial')
    plt.plot(var_tab, size_list_final, '.-', color='blue', lw=0.8, ms=5, label='final')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend(frameon=False)
    if var_name=='m1':
            plt.xlabel('$m_{eff}$')
    elif var_name=="n0_trapped":
        plt.xlabel('$n_0$ ($10^{13}$ cm$^{-2}$)')
    elif var_name=="sigma":
        plt.xlabel('$\sigma$ (nm)')
    plt.xlabel('$n_0$ ($10^{13}$ cm$^{-2}$)')
    plt.ylabel('size (nm)')
    plt.tight_layout()

    plots_dir = os.path.join(dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    output_path = os.path.join(plots_dir, f"size_comparison_{var_name}_z.png")
    plt.savefig(output_path, dpi=300)
    plt.show()
    