import cPickle

"""Hack to get names out of a cPickle serialised object saved as a text file"""
# Set file names:
genes = 'genes_of_interest.cPickle' # A python set()

with open(genes, 'r') as handle:
    gene_set = cPickle.load(handle)
    gene_set = sorted(gene_set)
    with open('genelist.txt', 'w') as outhandle:
        for gene in gene_set:
            print >>outhandle, gene