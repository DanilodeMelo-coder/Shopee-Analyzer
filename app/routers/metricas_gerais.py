from fastapi import APIRouter, HTTPException
from app.services.service_analyzer import analisar_ctr
import app.estado_atual as estado


router = APIRouter()


@router.get("/metricas-gerais")
async def metricas_gerais():
    
    if estado.df_atual is not None:
        resultado_ctr = analisar_ctr(estado.df_atual)

        return resultado_ctr

    else:
        raise HTTPException(status_code = 400, detail="Nenhuma planilha enviada!" )