# eec refers to English essay correction

from fastapi import APIRouter
from essaygenie import essay_genie
from app.schemas.essay import Essay
from app.schemas.base import Success


eec_router = APIRouter()

@eec_router.post("/plain_text", summary="纯文本英语作文批改")
async def plain_text_eec(essay: Essay):
    out = essay_genie.correct_essay(essay.model_dump())
    return Success(data = out)