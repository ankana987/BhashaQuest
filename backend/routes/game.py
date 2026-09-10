from fastapi import APIRouter
router=APIRouter()
@router.get('/languages')
def languages():return [{'id':'hi','name':'Hindi','native':'हिन्दी'},{'id':'en','name':'English','native':'English'},{'id':'bn','name':'Bengali','native':'বাংলা'}]
@router.get('/levels')
def levels():return [{'id':1,'areaId':'garden','title':'Meet Someone in the Garden','xp':50},{'id':2,'areaId':'garden','title':'Tea Stall Conversation','xp':70},{'id':3,'areaId':'campus','title':'Find Your Way Around Campus','xp':80}]
