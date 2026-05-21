import pandas as pd


def analisar_ctr(df: pd.dataFrame) -> list:
    ctr = df["CTR"].str.replace("%", "").astype(float)
    ruins = df[ctr > 2.0]

    return ruins[["Nome do Anúncio", "CTR"]].to_dict(orient="records")