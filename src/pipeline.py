import kagglehub
import shutil
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def carregar(caminho):
    path = kagglehub.dataset_download("rtatman/chocolate-bar-ratings")

    shutil.copytree(path, "data/raw", dirs_exist_ok=True)

    data = pd.read_csv(caminho)
    print(data.shape)

    return df

# def limpar(df):