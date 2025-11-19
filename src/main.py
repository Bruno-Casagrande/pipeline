from pipeline import carregar

CAMINHO = 'data/raw/flavors_of_cacao.csv'
PROCESSADO = 'data/processed/flavors_processed.parquet'

def main():
    df = carregar(CAMINHO)