import numpy as np
import pandas as pd
import os

import re


def fix_fortran_number(s):
    s = str(s).strip()

    # normalne E/D
    if "E" in s or "e" in s:
        return float(s)
    if "D" in s or "d" in s:
        return float(s.replace("D", "E").replace("d", "e"))

    # fortranowe 0.12345-301
    m = re.match(r"^([+-]?\d*\.?\d+)([+-]\d+)$", s)
    if m:
        return float(f"{m.group(1)}E{m.group(2)}")

    return float(s)


def load_2D_map(filename):
    df = pd.read_csv(
        filename,
        sep=r"\s+",
        comment="#",
        names=["x", "y", "density"],
        dtype=str
    )

    for col in ["x", "y", "density"]:
        df[col] = df[col].apply(fix_fortran_number)

    df = df.sort_values(["x", "y"])

    grid = df.pivot(
        index="y",
        columns="x",
        values="density"
    )

    return grid


def load_file(filepath):
    return pd.read_csv(
        filepath,
        sep=r"\s+",
        comment="#",
        header=None,
        names=["z", "fun"]
    )

def load_iter_make_list(filepath, max_iter):
    file_list = []
    for i in range(1,max_iter+1):
        file_list.append(load_file(f"{filepath}_{i}.dat"))
    return file_list