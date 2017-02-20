def findcaps(thetext):
	i = thetext[:-2].find("!")
	if i >= 0:
		if thetext[i+1].isupper() or thetext[i+2].isupper():
			thetext = thetext[:i+1] + findcaps(thetext[i+1:])
		else:
			thetext = thetext[:i] + thetext[i+1:]
			thetext = findcaps(thetext)
	return(thetext)
f = open('testfile1.txt','r+')
thetext = f.read()
f.close()
f = open('testfile1.txt','w')
f.write(findcaps(thetext).replace("!!", "!").replace("  ", " "))
f.close()
