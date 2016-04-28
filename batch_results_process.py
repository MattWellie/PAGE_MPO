
# Shabby script to read and split the results from the MPO results files
# This takes a TSV file and opens it as a dictionary, continuing to process and export the results

import csv

file_in = 'batch_query_no_infertile.tsv'
ddg2p = 'DDG2P.csv'
phenotype_col = 'mp_id'
human_col = 'human_gene_symbol'
mouse_col = 'marker_symbol'
results_dict = {}

# Open the file as a handle, and then use the csv.DictReader to open it with headings as keys
with open(file_in, 'r') as handle:
    dict = csv.DictReader(handle, delimiter='\t')
    for row in dict:
        mouse_set = set()
        human_set = set()
        phenotype = row[phenotype_col]
        
        # Get the mouse gene row, split and count
        mouse_roi = row[mouse_col]
        separated = mouse_roi.split('|')
        for x in separated:
            mouse_set.add(x)
        print '{} - Mouse genes: {}'.format(phenotype, len(mouse_set))

        # Get the human gene row, split and count        
        roi = row[human_col]
        separated = roi.split('|')
        for x in separated:
            human_set.add(x)
        print '{} - Human genes: {}'.format(phenotype, len(human_set))
        
        results_dict[phenotype] = {'human_set': human_set, 'mouse_set': mouse_set,
                                   'human_len': len(human_set), 'mouse_len': len(mouse_set)}
        
phenotypes = results_dict.keys()    

# This shouldn't be hard-coded, but I know there are only two phenotypes present
phen1 = phenotypes[0]
phen2 = phenotypes[1]

# Combined total (not excluding overlap)
print 'Combined human total: {}'.format(results_dict[phen1]['human_len'] + results_dict[phen2]['human_len'])

# Now combine the sets to check for any overlap
combined = results_dict[phen1]['human_set'].union(results_dict[phen2]['human_set'])
print 'Unique total: {}'.format(len(combined))

print 'Overlapping genes:'
overlaps = set()
for x in results_dict[phen1]['human_set']:
    for y in results_dict[phen2]['human_set']:
        if x == y:
            overlaps.add(x)
print overlaps

# Grab all the gene names from the DDG2P input file
ddg2p_set = set()
first_line = True
with open(ddg2p, 'r') as handle:
	for line in handle:
		if first_line:
		    first_line = False
		else:
		    ddg2p_set.add(line.split(',')[0])
		    
print 'Number of DDG2P genes: {}'.format(len(ddg2p_set))            

# Set values to count the total number of overlaps involved
phen_1_overlap = 0
phen_2_overlap = 0
# And a value to count the number overlapping both phenotypes
both_count = 0

for gene in ddg2p_set:
    both = False
    if gene in results_dict[phen1]['human_set']:
        print 'This gene is present in {}-Human and DDG2P: {}'.format(phen1, gene)
        phen_1_overlap += 1
        both = True
    if gene in results_dict[phen2]['human_set']:
        print 'This gene is present in {}-Human and DDG2P: {}'.format(phen2, gene)
        phen_2_overlap += 1
        if both:
            both_count += 1
        
# Total overlapping with each clinical phenotype:
print 'DDG2P overlap with {}: {}'.format(phen1, phen_1_overlap)
print 'DDG2P overlap with {}: {}'.format(phen2, phen_2_overlap)
print 'DDG2P overlap with both phenotypes: {}'.format(both_count)