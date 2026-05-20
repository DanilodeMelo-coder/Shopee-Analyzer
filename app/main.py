from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from fastapi.responses import JSONResponse
import io #tratar sem precisar salvar na memoria
import math

app = FastAPI()

@app.get("/")
async def home():
    return("Api funcionando")

@app.post("/upload-planilha")
async def upload_planilha(arquivo: UploadFile = File (...)):

    if not arquivo.filename.endswith((".xlsx", ".xls", ".csv")):
        raise HTTPException(status_code= 400, detail="Envie uma arquivo compativel(.xlsx, .xls ou .csv)")


    conteudo = await arquivo.read()

    try:
        if arquivo.filename.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(conteudo),  skiprows=7, encoding="utf-8-sig")
        else:
            df = pd.read_excel(io.BytesIO(conteudo),  skiprows=7, encoding="utf-8-sig")
    except:
        raise HTTPException(status_code=422, detail=f"Erro ao ler arquivo")

    #verificar se valor é nan ou float e troca para str
    def limpar_valor(v):
        if isinstance(v, float) and math.isnan(v):
            return ""
        return v

    preview = [
        {k: limpar_valor(v) for k, v in row.items()}
        for row in df.head(5).to_dict(orient="records")
    ]

    return JSONResponse(content={
        "arquivo": arquivo.filename,
        "linhas": len(df),
        "colunas": list(df.columns),
        "preview": preview
    })