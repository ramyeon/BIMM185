import sys
import math

#dictionary to translate nucleotides on reverse strands
dict = {'A':'T','T':'A','G':'C','C':'G'}

#read in whole genome data on a single line, removing new line characters
f = open(sys.argv[1],'r')
line = f.readline()
line = f.readline()
seq = ''
while line:
	line = line.rstrip()
	seq += line
	line = f.readline()
f = open(sys.argv[2],'r')
line = f.readline()
line = f.readline()

#read in annotation list, key is in form Product, Locus, Tag, seperated by | characters
#dictionary entry is strand, start, stop, in tuple form
protein_list = {}
name = ''
while line:
	prot = line.split('\t')
	name = '>'
	name += prot[8]
	name += '|'
	name += prot[6]
	name += '|'
	name += prot[7]
	protein_list[name] = (prot[4],int(prot[2]),int(prot[3]))
	line = f.readline()
	
#for each protein, get the sequence from the genome, translate if in reverse strand, and print as needed
for key in protein_list:
	data = protein_list[key]
	if data[0] == '+':
		toPrint = seq[data[1]-1:data[2]]
	else:
		holder = seq[data[1]-1:data[2]]
		toPrint = ''
		for i in range(len(holder)):
			toPrint += dict[holder[len(holder)-i-1]]
	print key.split('|')[2],'\t',toPrint
