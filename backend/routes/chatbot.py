from fastapi import APIRouter
from models.schemas import ChatRequest,ChatResponse
from services.ai_service import ask
router=APIRouter()
@router.post('/chat',response_model=ChatResponse)
async def chat(x:ChatRequest):return await ask(x.model_dump())
