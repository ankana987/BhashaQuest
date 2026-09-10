from fastapi import APIRouter
from models.schemas import EvaluationRequest,EvaluationResponse
from services.evaluation_service import evaluate
router=APIRouter()
@router.post('/evaluate-speech',response_model=EvaluationResponse)
def speech(x:EvaluationRequest):return evaluate(x.expectedPhrases,x.recognizedSpeech)
