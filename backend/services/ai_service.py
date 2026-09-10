import os,httpx,json
from dotenv import load_dotenv
load_dotenv()
def fallback(lang,obj):
 tea='tea' in obj.lower() or 'chai' in obj.lower()
 if tea:
  if lang=='Hindi':return {'response':'Let’s make it simple. Ask politely for tea.','phrase':'मुझे एक कप चाय चाहिए।','roman':'Mujhe ek cup chai chahiye.','meaning':'I would like a cup of tea.','hint':'Start with “Mujhe…”.'}
  if lang=='Bengali':return {'response':'Let’s make it simple. Ask politely for tea.','phrase':'আমার এক কাপ চা চাই।','roman':'Amar ek cup cha chai.','meaning':'I would like a cup of tea.','hint':'Start with “Amar…”.'}
  return {'response':'Ask politely for a cup of tea.','phrase':'I would like a cup of tea.','roman':'I would like a cup of tea.','meaning':'A polite tea order.','hint':'Start with “I would like…”.'}
 if lang=='Hindi':return {'response':'Start with a respectful greeting.','phrase':'नमस्ते','roman':'Namaste','meaning':'Hello / respectful greeting','hint':'Try the common respectful greeting.'}
 if lang=='Bengali':return {'response':'Start with a respectful greeting.','phrase':'নমস্কার','roman':'Nomoshkar','meaning':'Hello / respectful greeting','hint':'Try “Nomoshkar”.'}
 return {'response':'Start with a friendly greeting.','phrase':'Hello','roman':'Hello','meaning':'A friendly greeting','hint':'A simple “Hello” works.'}
async def ask(p):
 key,url,model=os.getenv('LLM_API_KEY'),os.getenv('LLM_API_URL'),os.getenv('LLM_MODEL','')
 if not key or not url:return fallback(p['targetLanguage'],p['objective'])
 try:
  body={'model':model,'messages':[{'role':'system','content':'You are BhashaQuest beginner language mentor. Keep answers short. Return JSON with response, phrase, roman, meaning, hint.'},{'role':'user','content':str(p)}],'temperature':.4}
  async with httpx.AsyncClient(timeout=20) as c:r=await c.post(url,headers={'Authorization':f'Bearer {key}'},json=body);r.raise_for_status();return json.loads(r.json()['choices'][0]['message']['content'])
 except Exception:return fallback(p['targetLanguage'],p['objective'])
