from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.service_upload import ler_planilha
from app.services.service_analyzer import analisar_ctr
import app.estado_atual as estado

router = APIRouter()



@router.post("/upload-planilha")
async def upload_planilha(arquivo: UploadFile = File (...)):

    if not arquivo.filename.endswith((".xlsx", ".xls", ".csv")):
        raise HTTPException(status_code= 400, detail="Envie uma arquivo compativel(.xlsx, .xls ou .csv)")


    conteudo = await arquivo.read()

    try:
        estado.df_atual = ler_planilha(conteudo, arquivo.filename)
    except:
        raise HTTPException(status_code=422, detail=f"Erro ao ler arquivo")

    resultado_ctr = analisar_ctr(estado.df_atual)

    return JSONResponse(content={
        "arquivo": arquivo.filename,
        "linhas": len(estado.df_atual),
        "colunas": list(estado.df_atual.columns),
        "preview": estado.df_atual.head(5).to_dict(orient="records"), "CTR": resultado_ctr
    }) 


