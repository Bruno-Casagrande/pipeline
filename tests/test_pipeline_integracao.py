import pandas as pd
from  pacote_projeto.pipeline import carregar, limpar, engenharia

def test_completo():
    df = pd.DataFrame({
        "rating": [2.5, 3.8, 4.0],
        "cocoa_percent": ["70%", "60%", "85%"]
    })

    df2 = limpar(df)
    df3 = engenharia(df2)

    assert "rating_zscore" in df3.columns
    assert "acima_media" in df3.columns