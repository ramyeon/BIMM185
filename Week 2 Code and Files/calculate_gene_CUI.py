import sys
import numpy as np

f = open(sys.argv[1],'r')

line = f.readline().rstrip()

global_data = []
line = line.split('\t')

#read first line of data, global codon usage
for i in range(1,len(line)-1):
	global_data.append(float(line[i])/float(line[len(line)-1]))

#read each line iteratively, to save memory
line = f.readline().rstrip()
while line:
	line = line.split('\t')
	data = []
	for i in range(1,len(line)-1):
		data.append(float(line[i])/float(line[len(line)-1]))
	#calculate CUI as dot product of global array and gene frequencies
	print line[0],'\t',np.dot(global_data,data)	
	line = f.readline().rstrip()
