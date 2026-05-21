import pandas as pd


def analisar_ctr(df: pd.dataFrame) -> list:
    ctr = df["CTR"].str.replace("%", "").astype(float)
    ruins = df[ctr > 2.0]

    return ruins[["Nome do Anúncio", "CTR"]].to_dict(orient="records")


def analisar_taxaconversao(df: pd.dataFrame) -> list:
    tx_conversao = df["Taxa de conversão"].str.replace("%", "").astype(float)

    df = df.copy()
    df["classificacao"] = tx_conversao.apply(classificar_taxa)

    ruins = df[df["classificacao"] == "Ruim"]

    return ruins[["Nome do Anúncio", "Taxa de conversão", "classificacao"]].to_dict(orient="records")


    


def classificar_taxa(tx: float) -> str:
    if tx < 1:
        return "Ruin"
    elif tx > 1 and tx < 2:
        return "Aceitavel"
    elif tx > 2 and tx < 4:
        return "Bom"
    else:
        return "Excelente"