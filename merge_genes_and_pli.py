import cPickle, csv
import numpy as np
import matplotlib.pyplot as plt

"""
This will take the genes implicated in the mouse phenotypes, and look them up in
the file containing all the pLI (ExAC paper) details to look for trends. This would
probably be better done in R to be honest... I need to practice.
"""

# Set file names:
genes = 'genes_of_interest.cPickle' # A python set()
ddg2p_overlap = 'ddg2p_overlap_genes.cPickle'
pli = 'pli.txt' # Tab-delimited text file
pli_values = []
pli_gene_dict = {} # Keep a store, decide what to do with it later
ddg2p_pli = []

with open(genes, 'r') as handle:
    gene_set = cPickle.load(handle)
    gene_set = sorted(gene_set)

with open(ddg2p_overlap, 'r') as handle:
    ddg2p_overlap_genes = cPickle.load(handle)
    ddg2p_overlap_genes = sorted(ddg2p_overlap_genes)

# Now import the appropriate columns from the pLI file
# Using default csv module, will take a while. Pandas not installed
# As this only has to be iterated over once, maybe not too bad
with open(pli, 'rU') as handle:
    pli_dict = csv.DictReader(handle, delimiter='\t')
    # Columns of interest will be ['gene', 'chr', 'pLI']

    for row in pli_dict:
        gene = row['gene']
        if gene in gene_set:
            # Then do something with the values
            pli_value = float(row['pLI'])
            pli_values.append(pli_value)
            pli_gene_dict[gene] = pli_value
        if gene in ddg2p_overlap_genes:
            ddg2p_pli.append(pli_value)

pli_sorted = sorted(pli_values)
lowest = pli_sorted[0]
highest = pli_sorted[-1]
print "Lowest pLI value: {}".format(lowest)
print "Highest pLI value: {}".format(highest)

for x in pli_gene_dict:
    if pli_gene_dict[x] < 0.00001:
        print "{} - {}".format(pli_gene_dict[x], x)

print " ----- "

for x in pli_gene_dict:
    if pli_gene_dict[x] == highest:
        print "highest - {}".format(x)
    elif pli_gene_dict[x] == lowest:
        print "lowest - {}".format(x)

line = plt.figure()
plt.plot(sorted(ddg2p_pli), 'o')
plt.ylabel('pLI Score')
plt.xlabel('Gene (sorted by pLI score)')
plt.title('A scatter plot of all pLI scores')

plt.show()
