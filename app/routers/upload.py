from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.service_upload import ler_planilha
from app.services.service_analyzer import analisar_ctr

router = APIRouter()



@router.post("/upload-planilha")
async def upload_planilha(arquivo: UploadFile = File (...)):

    if not arquivo.filename.endswith((".xlsx", ".xls", ".csv")):
        raise HTTPException(status_code= 400, detail="Envie uma arquivo compativel(.xlsx, .xls ou .csv)")


    conteudo = await arquivo.read()

    try:
        df = ler_planilha(conteudo, arquivo.filename)
    except:
        raise HTTPException(status_code=422, detail=f"Erro ao ler arquivo")

    resultado_ctr = analisar_ctr(df)

    return JSONResponse(content={
        "arquivo": arquivo.filename,
        "linhas": len(df),
        "colunas": list(df.columns),
        "preview": df.head(5).to_dict(orient="records"), "CTR": resultado_ctr
    }) 


