import os
import math

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
from matplotlib.cm import get_cmap
import matplotlib.gridspec as gridspec

## Font
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman', 'Times', 'DejaVu Serif']
rcParams['font.size'] = 9

rcParams['axes.labelsize'] = 9
rcParams['axes.titlesize'] = 9
rcParams['legend.fontsize'] = 8
rcParams['xtick.labelsize'] = 8
rcParams['ytick.labelsize'] = 8

## Lines
rcParams['lines.linewidth'] = 1.1
rcParams['lines.solid_joinstyle'] = 'miter'
rcParams['lines.antialiased'] = True
rcParams['lines.markersize'] = 4

## Axes
rcParams['axes.linewidth'] = 0.8

## Legend
rcParams['legend.frameon'] = False
rcParams['legend.loc'] = 'best'

## Ticks
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = True
rcParams['ytick.right'] = True

rcParams['xtick.major.size'] = 4
rcParams['ytick.major.size'] = 4
rcParams['xtick.minor.size'] = 2
rcParams['ytick.minor.size'] = 2

rcParams['xtick.major.width'] = 0.8
rcParams['ytick.major.width'] = 0.8
rcParams['xtick.minor.width'] = 0.6
rcParams['ytick.minor.width'] = 0.6

rcParams['xtick.minor.visible'] = True
rcParams['ytick.minor.visible'] = True

## Figure
rcParams['figure.figsize'] = (3.35, 2.5)
rcParams['figure.dpi'] = 300
rcParams['savefig.dpi'] = 300

## Colormaps
cm_inferno = get_cmap("inferno")
cm_plasma = get_cmap("plasma")
cm_viridis = get_cmap("viridis")
cm_seismic = get_cmap("seismic")
cm_tab10 = get_cmap("tab10")

### Palettes from color-hex.com/ 
c_google = ['#008744', '#0057e7', '#d62d20', '#ffa700'] # G, B, R, Y # https://www.color-hex.com/color-palette/1872 
c_twilight = ['#363b74', '#673888', '#ef4f91', '#c79dd7', '#4d1b7b'] # https://www.color-hex.com/color-palette/809
c_palette = ["#780000","#c1121f","#fdf0d5","#003049","#669bbc"]


def plot_2D_map(df, filename, title):
    plt.imshow(
        df.values.T,
        origin="lower",
        aspect="equal",
        extent=[
            df.index.min(),
            df.index.max(),
            df.columns.min(),
            df.columns.max()
        ],
        cmap="inferno"
    )

    plt.xlabel("x (nm)")
    plt.ylabel("y (nm)")
    plt.title(title)
    plt.colorbar()
    plt.tight_layout()

    plt.savefig(f"{filename}.png")

    plt.show()

def crossection_in_iters(data, max_iter, filename):
    init_loaded = False
    if isinstance(data, (str, os.PathLike)):
        from loader import load_iter_make_list, load_file
        # load iterations
        iter_frames = load_iter_make_list(data, max_iter)

        # try to also load the initial state file named '<prefix>_init.dat'
        init_path = f"{filename}_init.dat"
        frames = list(iter_frames)
        if os.path.exists(init_path):
            try:
                init_frame = load_file(init_path)
                frames.insert(0, init_frame)
                init_loaded = True
            except Exception as e:
                print(f"failed to load init file {init_path}: {e}")
    else:
        if not isinstance(data, (list, tuple)):
            raise TypeError("data must be a list/tuple of frames or a filepath prefix")

        frames = list(data)[:max_iter]
    if not frames:
        return

    fig, ax = plt.subplots(figsize=(6.5, 4), squeeze=False)
    ax = ax[0, 0]

    colors = cm_plasma(np.linspace(0, 1, len(frames)))
    
    x_label = None
    y_label = None

    for i, (frame, color) in enumerate(zip(frames, colors)):
        if hasattr(frame, "iloc"):
            x = frame.iloc[:, 0]
            y = frame.iloc[:, 1]
            x_label = frame.columns[0]
            y_label = frame.columns[1]
        else:
            x = frame[0]
            y = frame[1]
            x_label = "col 1"
            y_label = "col 2"

        if init_loaded:
            label = "init" if i == 0 else f"iter {i}"
        else:
            label = f"iter {i}"

        ax.plot(x, y, label=label, color=color)

        # compute 90% width (z05, z95) like in your example
        try:
            z = np.asarray(x)
            rho = np.asarray(y)
            cdf = np.cumsum(rho)
            if cdf.size == 0 or cdf[-1] == 0:
                width90 = float('nan')
            else:
                cdf = cdf / cdf[-1]
                z05 = z[np.searchsorted(cdf, 0.05)]
                z95 = z[np.searchsorted(cdf, 0.95)]
                width90 = z95 - z05
            print(f"{label}: width90 = {width90}")
        except Exception as e:
            print(f"{label}: width90 computation failed: {e}")

    ax.set_xlabel(x_label or "x")
    ax.set_ylabel(y_label or "y")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()
    
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    fig.savefig(f"{filename}.png", dpi=300)
    plt.show()

def plot_epsilon(file_list, nx_list):
    if len(file_list) != len(nx_list):
        raise ValueError("file_list and nx_list must have the same length")

    if not file_list:
        return

    for data, label in zip(file_list, nx_list):
        if isinstance(data, dict):
            z = data["z"]
            fun = data["fun"]
        elif hasattr(data, "columns") and "z" in data.columns and "fun" in data.columns:
            z = data["z"]
            fun = data["fun"]
        else:
            raise TypeError("each element of file_list must contain 'z' and 'fun' values")

        plt.plot(z, fun, label=str(label))

    plt.xlabel("z")
    plt.ylabel("fun")
    plt.legend()
    plt.tight_layout()
    plt.show()

