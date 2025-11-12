import kagglehub
import shutil
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("rtatman/chocolate-bar-ratings")

raw_data_folder = "data/raw"

shutil.copytree(path, raw_data_folder, dirs_exist_ok=True)

print("Caminho do arquivo dataset:", path)
print("Copiado para: ", os.path.abspath(raw_data_folder))

data = pd.read_csv('C:/Users/Bruno/Desktop/nome/projeto/pipeline/data/raw/flavors_of_cacao.csv')
print(data.shape)