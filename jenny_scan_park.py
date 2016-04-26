import cPickle

# script to read in a list of gene names, and check a list of de novo variants 
# from DF1 against them to find any overlaps

input_file = 'jenny_query.tsv'
genes = 'genes_of_interest.cPickle'

with open(genes, 'r') as handle:
    genelist = cPickle.load(handle)

# genelist is a set()

with open(input_file, 'r') as handle:
    
    for line in handle:
        line_list = line.split('\t')
        if line_list[0] == 'id':
            print 'ID'
        else:
            line_gene_list = line_list[7].split('|')
            for gene in line_gene_list:
                if gene in genelist:
                    print line    
                    break