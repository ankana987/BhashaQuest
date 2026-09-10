from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chatbot import router as chatbot
from routes.game import router as game
from routes.speech import router as speech
app=FastAPI(title='BhashaQuest API')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(chatbot,prefix='/api');app.include_router(game,prefix='/api');app.include_router(speech,prefix='/api')
@app.get('/')
def root():return {'name':'BhashaQuest API','status':'ok'}
