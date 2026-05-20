import pandas as pd
import io
import math

def limpar_valor(v):
    if isinstance(v, float) and math.isnan(v):
        return ""
    return v

def encontrar_inicio(conteudo: bytes) -> int:
    linhas = conteudo.decode("utf-8-sig").splitlines()
    for i, linha in enumerate(linhas):
        if linha.startswith("#,") or linha.startswith("#\t"):
            return i
    return 7

def ler_planilha(conteudo: bytes, filename: str) -> pd.DataFrame:
    if filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(conteudo), skiprows=encontrar_inicio(conteudo), encoding="utf-8-sig")
    else:
        df = pd.read_excel(io.BytesIO(conteudo), skiprows=7)

    df = df.apply(lambda col: col.map(limpar_valor))

    return df