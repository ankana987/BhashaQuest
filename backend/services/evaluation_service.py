import re,unicodedata
def norm(s):return re.sub(r'\s+',' ',re.sub(r'[^\w\s]',' ',unicodedata.normalize('NFD',s.lower()))).strip()
def sim(a,b):
 a,b=norm(a),norm(b)
 if not a or not b:return 0
 if a==b:return 100
 if a in b or b in a:return 88
 A,B=set(a.split()),set(b.split());return round(200*len(A&B)/max(len(A)+len(B),1))
def evaluate(expected,spoken):
 score=max([sim(x,spoken) for x in expected] or [0]);return {'score':score,'correct':score>=70,'feedback':'Excellent!' if score>=90 else 'Good job!' if score>=70 else 'Almost there — try again.','mistakes':[] if score>=70 else ['Try matching the model phrase more closely.']}
