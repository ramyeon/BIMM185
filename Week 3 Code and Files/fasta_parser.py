#used biopython, regex, and gzip
from Bio import SeqIO
import re
import gzip

#gzip opener for windows
f = gzip.open('EColi_Proteins.faa.gz','r')

#print everything as needed
for record in SeqIO.parse(f,'fasta'):
	print record.id,'\t',record.seq