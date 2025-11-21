import pandas as pd
from pacote_projeto.pipeline import limpar

def test_remove_dup():
    df = pd.DataFrame({
        "rating": [3.0, 3.0],
        "cocoa_percent": ["70%", "70%"]
    })

    df_limpo = limpar(df)
    assert len(df_limpo) == 1