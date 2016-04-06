import csv, cPickle
import numpy as np
import matplotlib.pyplot as plt

"""
Something quick to get a set of genes from a csv file
"""

file_in = 'batch_tsv.txt'
field = 'human_gene_symbol'
ddg2p = 'DDG2P.csv'
annotations = 'annotations.cPickle'
gene_set = set()
gene_duplicates = set()

# Import the file
with open(file_in, 'rU') as handle:
    dict = csv.DictReader(handle, delimiter='\t')
    
    for row in dict:
        gene_list = row[field].split('|')
        print '{}: {}'.format(row['mp_id'], len(gene_list))
        for gene in gene_list:
            if gene in gene_set:
                gene_duplicates.add(gene)
            else:
                gene_set.add(gene)
                    
print 'Unique genes found: {}'.format(len(gene_set))
print '{} genes were present in multiple categories:\n'.format(len(gene_duplicates))
print gene_duplicates

# Grab all the gene names from the DDG2P input file
ddg2p_set = set()
first_line = True
with open(ddg2p, 'r') as handle:
	for line in handle:
		if first_line:
		    first_line = False
		else:
		    ddg2p_set.add(line.split(',')[0])
print len(ddg2p_set)		            
		    
# Identify any overlapping genes:
ddg2p_overlap = set()
for gene in gene_set:
    if gene in ddg2p_set:
        ddg2p_overlap.add(gene)

        
print 'Total phenotype genes overlapping DDG2P: {}'.format(len(ddg2p_overlap))
print ddg2p_overlap

# Import and use the pickled set of annotations from the DDD project
# This contains the HI, HS, and phenotype details where available
with open(annotations, 'r') as handle:
    anno_dict = cPickle.load(handle)
    
# Create a list to hold all the 
hi_scores = []
annotated_genes = set()
not_found = set()
for gene in ddg2p_overlap:
    found = False
    for chromosome in anno_dict:
        if gene in anno_dict[chromosome]:
            found = True
            annotated_genes.add(gene)
            print '\nHI Gene Annotations for {}'.format(gene)
            ann_keys = anno_dict[chromosome][gene].keys()
            if 'hi_score' in ann_keys: 
                print '\tHI: {}'.format(anno_dict[chromosome][gene]['hi_score'])
                hi_scores.append(float(anno_dict[chromosome][gene]['hi_score']))
            if 'hs_score' in ann_keys: 
                print '\tHS: {}'.format(anno_dict[chromosome][gene]['hs_score'])
            if 'diseases' in ann_keys: 
                for disease in anno_dict[chromosome][gene]['diseases']:
                    print '\t{}'.format(disease)
    if not found:
        not_found.add(gene)
        
print '{}/{} Genes had annotations available'.format(len(annotated_genes), len(ddg2p_overlap))
print '{} Genes didn\'t have annotations:'.format(len(not_found))
print not_found
print '{} Genes had HI scores associated with them'.format(len(hi_scores))   

# Maybe try and plot this as a graph 
line = plt.figure()
plt.plot(sorted(hi_scores), 'o')
plt.ylabel('HI Score')
plt.xlabel('Gene (sorted by HI score)')
plt.title('A scatter plot of all HI scores')
plt.show()