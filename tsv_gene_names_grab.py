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
all_output = 'tsv_names_summary_out.txt'
gene_set = set()
gene_duplicates = set()
printed_lines = []

# Import the file
with open(file_in, 'rU') as handle:
    dict = csv.DictReader(handle, delimiter='\t')
    
    for row in dict:
        gene_list = row[field].split('|')
        printed_lines.append('{} - {}: {}'.format(row['mp_id'], row['mp_definition'], len(gene_list)))
        for gene in gene_list:
            if gene in gene_set:
                gene_duplicates.add(gene)
            else:
                gene_set.add(gene)
                    
printed_lines.append('Unique genes found: {}'.format(len(gene_set)))
printed_lines.append('{} genes were present in multiple categories:\n'.format(len(gene_duplicates)))
printed_lines.append(gene_duplicates)

# Dump the gene set to a pickle file
with open('genes_of_interest.cPickle', 'w') as handle:
    cPickle.dump(gene_set, handle)

# Grab all the gene names from the DDG2P input file
ddg2p_set = set()
first_line = True
with open(ddg2p, 'r') as handle:
	for line in handle:
		if first_line:
		    first_line = False
		else:
		    ddg2p_set.add(line.split(',')[0])
		    
# Identify any overlapping genes:
ddg2p_overlap = set()
for gene in gene_set:
    if gene in ddg2p_set:
        ddg2p_overlap.add(gene)

# Dump the gene set to a pickle file
with open('ddg2p_overlap_genes.cPickle', 'w') as handle:
    cPickle.dump(ddg2p_overlap, handle)

        
printed_lines.append('Total phenotype genes overlapping DDG2P: {}'.format(len(ddg2p_overlap)))
printed_lines.append(ddg2p_overlap)

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
            printed_lines.append('\nHI Gene Annotations for {}'.format(gene))
            ann_keys = anno_dict[chromosome][gene].keys()
            if 'hi_score' in ann_keys: 
                printed_lines.append('\tHI: {}'.format(anno_dict[chromosome][gene]['hi_score']))
                hi_scores.append(float(anno_dict[chromosome][gene]['hi_score']))
            if 'hs_score' in ann_keys: 
                printed_lines.append('\tHS: {}'.format(anno_dict[chromosome][gene]['hs_score']))
            if 'diseases' in ann_keys: 
                for disease in anno_dict[chromosome][gene]['diseases']:
                    printed_lines.append('\t{}'.format(disease))
    if not found:
        not_found.add(gene)
        
printed_lines.append('\n{}/{} Genes had annotations available'.format(len(annotated_genes), len(ddg2p_overlap)))
printed_lines.append('{} Genes didn\'t have annotations:'.format(len(not_found)))
printed_lines.append(not_found)

with open(all_output, 'wb') as handle:
    for line in printed_lines:
        print >>handle, line

# Maybe try and plot this as a graph 
line = plt.figure()
plt.plot(sorted(hi_scores), 'o')
plt.ylabel('HI Score')
plt.xlabel('Gene (sorted by HI score)')
plt.title('A scatter plot of all HI scores')
plt.show()