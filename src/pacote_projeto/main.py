from pipeline import carregar, limpar, engenharia, salvar
from visualizar import gerar_figuras

CAMINHO = 'data/raw/flavors_of_cacao.csv'
PROCESSADO = 'data/processed/flavors_processed.parquet'

def main():
    df = carregar(CAMINHO)
    df = limpar(df)
    df = engenharia(df)
    
    gerar_figuras(df)
    
    df_back = salvar(df, PROCESSADO)
    print("Pipeline rodado com sucesso! Linhas:", len(df_back))

if __name__ == "__main__":
    main()