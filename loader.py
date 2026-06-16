import numpy as np
import pandas as pd
import os

def load_2D_map(filename):
    df = pd.read_csv(
        filename,
        sep=r"\s+",
        comment="#",
        names=["x", "y", "density"]
    )

    df = df.sort_values(["x", "y"])

    grid = df.pivot_table(
        index="y",
        columns="x",
        values="density",
        aggfunc="mean"
    )

    return grid