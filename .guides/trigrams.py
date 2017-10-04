import sys

clist = []

def getCiphertxt():
        return(sys.stdin.read())

def getWords(c):
	tmp = []
	for w in c.split():
		#if len(w) >= 3:
		if len(w) == 3:
			tmp.append(w)
	return tmp	

def getTrigrams(clist):
	tmp = []
	for c in clist:
# only look at first 3 chars for now - 10/3/17 pgs
#		N = len(c)-3
#		for i in range(N+1):
#			tmp.append(c[i:i+3])
		tmp.append(c[0:3])
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
#	if trigrams[t] > 1:
#		print trigrams[t],t
	print trigrams[t],t
