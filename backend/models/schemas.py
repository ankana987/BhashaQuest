from pydantic import BaseModel,Field
class ChatRequest(BaseModel): message:str=Field(min_length=1);targetLanguage:str;nativeLanguage:str;level:int;location:str;objective:str;previousMistakes:list[str]=[]
class ChatResponse(BaseModel): response:str;phrase:str='';roman:str='';meaning:str='';hint:str=''
class EvaluationRequest(BaseModel): expectedPhrases:list[str];recognizedSpeech:str;targetLanguage:str;level:int
class EvaluationResponse(BaseModel): score:int;correct:bool;feedback:str;mistakes:list[str]=[]
