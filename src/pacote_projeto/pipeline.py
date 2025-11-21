import kagglehub
import shutil
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def carregar(caminho):
    path = kagglehub.dataset_download("rtatman/chocolate-bar-ratings")

    shutil.copytree(path, "data/raw", dirs_exist_ok=True)

    try:
        df = pd.read_csv(caminho)
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar arquivo: {e}")

    df.columns = (
         df.columns
        .str.replace(r'\s+', ' ', regex=True)
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )

    return df

def limpar(df):
    df = df.copy()

    df = df.drop_duplicates()

    df["cocoa_percent"] = (
        df["cocoa_percent"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    df["cocoa_percent"] = pd.to_numeric(df["cocoa_percent"], errors="coerce")

    df = df.fillna({
        "cocoa_percent": df["cocoa_percent"].median(),
        "rating": df["rating"].median()
    })
    
    return df

def engenharia(df):
    df = df.copy()
    df["rating_zscore"] = (df["rating"] - df["rating"].mean()) / df["rating"].std()
    df["acima_media"] = (df["rating"] > df["rating"].mean()).astype(int)
    return df


def salvar(df, caminho_parquet):
    df.to_parquet(caminho_parquet, index=False)

    df_back = pd.read_parquet(caminho_parquet)
    return df_back