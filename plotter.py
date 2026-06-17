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
        aspect="auto",
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