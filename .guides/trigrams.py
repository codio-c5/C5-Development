import sys

clist = []

def getCiphertxt():
        return(sys.stdin.read())

def getWords(c):
	tmp = []
	for w in c.split():
		if len(w) >= 3:
			tmp.append(w)
	return tmp	

def getTrigrams(clist):
	tmp = []
	for c in clist:
		N = len(c)-3
		for i in range(N+1):
			tmp.append(c[i:i+3])
	return tmp

ctxt = getCiphertxt()
clist = getWords(ctxt)
tlist = getTrigrams(clist)

trigrams = {}
for t in tlist:
	if t in trigrams.keys():
		trigrams[t] += 1
	else:
		trigrams[t] = 1

for t in trigrams:
	if trigrams[t] > 1:
		print trigrams[t],t