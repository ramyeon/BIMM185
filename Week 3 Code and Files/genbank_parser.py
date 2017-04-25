#used biopython, regex, and gzip (no bash)
from Bio import SeqIO
import re
import gzip

#list to iterate through the fields in order
info_list = ['gene','locus_tag','gene_synonym','product','taxon','EC_number','db_xref']

#gzip opener (I used windows, so no bash)
f = gzip.open('EColi_Genome.gbff.gz','r')

#function to format fields nicely, remove all brackets and apostrophes, cat multiple entries with a single comma
def format_nicely(s):
	t = s[1:len(s)-2]
	
	while "'" in t:
		t = t.replace("'",'')
	while ", " in t or "; " in t:
		t = t.replace("; ",',')
		t = t.replace(", ",',')
	
	return t

#only one record in EColi file, technically not necessary to iterate but more failsafe for other files	
for record in SeqIO.parse(f,'gb'):
	
	#for each feature in EColi
	for feature in record.features:
		
		taxon = 'NULL'
		#if feature is source, get taxon with a regex
		if feature.type == 'source':
			if 'db_xref' in feature.qualifiers:
				m = re.search("([^']+)",feature.qualifiers['db_xref'][0].split(':')[1])
				taxon = m.group(0)
		
		#if feature is a CDS, get necessary fields in order
		if feature.type == 'CDS':
			
			#lots of try/except blocks to print fields or error messages. used NULL instead of - to reduce confounding with strand
			#print protein_id
			try:
				print format_nicely(str(feature.qualifiers['protein_id'])),'\t',
			except KeyError:
				print 'Pseudo','\t',
			
			#print location
			try:
				location_holder = str(feature.location)
				location_holder = location_holder.split('(')
				print location_holder[0][1:len(location_holder[0])-1],'\t',location_holder[1][0],'\t',
			except:
				print 'NULL','\t','NULL','\t',
			
			#print everything in the info_list named above
			for x in info_list:
				#taxon is constant for each source, print where necessary
				if x != 'taxon':
					try:
						print format_nicely(str(feature.qualifiers[x])),'\t',
					except:
						print 'NULL','\t',
				else:
					if taxon:
						print taxon,'\t',
			print ''
						#print feature