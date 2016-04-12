import csv, cPickle
import numpy as np
import matplotlib.pyplot as plt

"""
    Something quick to get a set of genes from a csv file
    """

file_in = 'batch_tsv.txt'
pli = 'pli.txt' # Tab-delimited text file
gene_set = set()
pli_store = {}
phenotype_dict = {}

# Now import the appropriate columns from the pLI file into a dict
with open(pli, 'rU') as handle:
    pli_dict = csv.DictReader(handle, delimiter='\t')
    for row in pli_dict:
        gene = row['gene']
        pli_value = float(row['pLI'])
        pli_store[gene] = pli_value

# Import the file of phenotype-genes associations from MPO
with open(file_in, 'rU') as handle:
    # Open as a dictionary with default headers
    dict = csv.DictReader(handle, delimiter='\t')
    
    for row in dict:
        gene_list = row['human_gene_symbol'].split('|')
        temp = []
        for gene in gene_list:
            if gene in pli_store:
                temp.append(pli_store[gene])
    
        phenotype_dict[row['mp_id']] = temp

        # Now plot each phenotype's pli scores separately
        line = plt.figure()
        plt.plot(sorted(temp), 'o')
        plt.ylabel('pLI Score')
        plt.xlabel('Gene (sorted by pLI score)')
        plt.title('pLI scores for {}'.format(row['mp_id']))
        plt.show()