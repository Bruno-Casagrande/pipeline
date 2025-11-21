import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_figuras(df, pasta="imagens"):

    os.makedirs(pasta, exist_ok=True)

    plt.figure(figsize=(8,5))
    sns.histplot(df["rating"], bins=20)
    plt.title("Distribuição das notas")
    plt.savefig(f"{pasta}/hist_rating.png")

    plt.figure(figsize=(8,5))
    sns.scatterplot(x="cocoa_percent", y="rating", data=df)
    plt.title("Percentual de cacau vs Nota")
    plt.savefig(f"{pasta}/scatter_cocoa_rating.png")

    plt.figure(figsize=(8,5))
    df["company_location"].value_counts().head(10).sort_values().plot(kind="barh")
    plt.title("Top 10 países produtores")
    plt.xlabel("Quantidade")
    plt.ylabel("Pais")
    plt.tight_layout()
    plt.savefig(f"{pasta}/top_paises.png")
