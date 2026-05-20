import pandas as pd
import io #tratar sem precisar salvar na memoria
import math

#verificar se valor é nan ou float e troca para str
def limpar_valor(v):
    if isinstance(v, float) and math.isnan(v):
        return ""
    return v


def ler_planilha(conteudo: bytes, filename: str) -> pd.DataFrame:
    if filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(conteudo),  skiprows=7, encoding="utf-8-sig")
    else:
        df = pd.read_excel(io.BytesIO(conteudo),  skiprows=7)

    df = df.apply(lambda col: col.map(limpar_valor))

    return df

