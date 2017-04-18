import sys
import copy

f = open('tabbed_DNA_sequences.txt','r')
line = f.readline().rstrip()

global_codon_dict = {}
codon_dict = {}

#lookups to convert nucleotides into numerals and back
nucleotide_dict = {'A':0,'C':1,'G':2,'T':3}
inv_nucleotide_dict = {0:'A',1:'C',2:'G',3:'T'}

#populate our dictionaries with all possible codons (in alphabetical order)
for i in range(4):
	for j in range(4):
		for k in range(4):
			codon = ''
			codon += inv_nucleotide_dict[i]
			codon += inv_nucleotide_dict[j]
			codon += inv_nucleotide_dict[k]
			global_codon_dict[codon] = 0
			codon_dict[codon] = 0	

#for each line, calculate info
while line:
	data = line.split('\t')
	if len(data[1])%3 == 0:
		#check for sequences that are not %3 
		#print data[0],len(data[1]),' is not divisible by 3'
		gene_data_frequencies = copy.deepcopy(codon_dict)
		for i in range(len(data[1])/3):
			codon = data[1][i*3:i*3+3]
			gene_data_frequencies[codon] += 1
			global_codon_dict[codon] += 1
		#check if the sequence has multiple stop codons
		if gene_data_frequencies['TGA'] + gene_data_frequencies['TAA'] + gene_data_frequencies['TAG'] > 1:
			a = 0
			# print data[0],' has multiple stop codons', gene_data_frequencies['TGA'] + gene_data_frequencies['TAA'] + gene_data_frequencies['TAG']
		else:
			print data[0],'\t',
			for key in gene_data_frequencies:
				print gene_data_frequencies[key],'\t',
			print len(data[1])/3
	line = f.readline().rstrip()
num_codons = 0

#print global frequencies
print 'Global Frequencies','\t',
for key in global_codon_dict:
	num_codons += global_codon_dict[key]
	print global_codon_dict[key],'\t',
print num_codons
