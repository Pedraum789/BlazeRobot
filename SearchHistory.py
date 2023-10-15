_D='https://blaze-1.com/api/crash_games/history'
_C='SAME'
_B='crash_point'
_A='records'
import requests,json
def verifyToBuy(waitCrash,autoStop):
	A=waitCrash;B=0;C=requests.get(_D)
	if C.status_code==200:
		D=json.loads(C.text)
		for E in range(A):
			F=float(D[_A][E][_B])
			if F<autoStop:B+=1
		return B>=A
	return False
def getStatus(waitCrash,autoStop):
	B=autoStop;A=waitCrash;C=0;E=requests.get(_D)
	if E.status_code==200:
		D=json.loads(E.text)
		for F in range(A):
			G=float(D[_A][F+1][_B])
			if G<B:C+=1
		if float(D[_A][0][_B])>=B and C>=A:return'WIN'
		elif float(D[_A][0][_B])<B and C>=A:return'LOSE'
		else:return _C
	return _C
def getLastIdHistory():
	A=requests.get(_D)
	if A.status_code==200:B=json.loads(A.text);return B[_A][0]['id']
	return''
def getStatusById(waitCrash,autoStop,lastId,bought):
	E=autoStop;D=waitCrash
	if not bought:return _C
	F=0;G=requests.get(_D)
	if G.status_code==200:
		B=json.loads(G.text);A=0
		for C in range(len(B[_A])):
			if lastId==B[_A][C]['id']:A=C;break
		if A!=0:A=A-1
		for C in range(A,A+D):
			H=float(B[_A][C+1][_B])
			if H<E:F+=1
		if float(B[_A][A][_B])>=E and F>=D:return'WIN'
		elif float(B[_A][A][_B])<E and F>=D:return'LOSE'
		else:return _C
	return _C