import os

#create list of all directories in current dir
directory_list = [dI for dI in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(),dI))]

finaldict = {}

#iterate through directory list
for dI in directory_list:
	#generate filepath (./dir/dir/report.tbl)
	filepath = '%s/%s/%s/report.tbl'%(os.getcwd(),dI,dI) 
	f = open(filepath,'r')
	#get 3rd line
	for i in range(3):
		line = f.readline()
	#get 4th field
	score = line.split('\t')[3]
	#add data to dictionary
	if score in finaldict:
		finaldict[score].append(dI)
	else:
		finaldict[score] = [dI]
#sort all directory names alphanumerically
for key in finaldict:
	finaldict[key] = sorted(finaldict[key])
#sort field data in descending order
keylist = finaldict.keys()
keylist = sorted(keylist,reverse=True)
#print data according to specifications
for key in keylist:
	for dI in finaldict[key]:
		print dI,'\t',key 
