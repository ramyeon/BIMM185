import os

directory_list = [dI for dI in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(),dI))]

finaldict = {}

for dI in directory_list:
	filepath = '%s/%s/%s/report.tbl'%(os.getcwd(),dI,dI) 
	f = open(filepath,'r')
	for i in range(3):
		line = f.readline()
	score = line.split('\t')[3]
	if score in finaldict:
		finaldict[score].append(dI)
	else:
		finaldict[score] = [dI]
for key in finaldict:
	finaldict[key] = sorted(finaldict[key])

keylist = finaldict.keys()
keylist = sorted(keylist,reverse=True)
for key in keylist:
	for dI in finaldict[key]:
		print dI,'\t',key 
