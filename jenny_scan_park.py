import cPickle, os, csv

# script to read in a list of gene names, and check a list of de novo variants 
# from DF1 against them to find any overlaps

input_file = 'jenny_query.tsv'
pli_store = {}
files = [file for file in os.listdir('.') if file.split('_')[0] == 'park']

# Create a dictionary object to hold the full contents of the file, indexed by gene
jenny = {}
with open(input_file, 'r') as handle:
    for line in handle:
        line_list = line.split('\t')
        if line_list[0] == 'id':
            pass
        else:
            line_gene_list = line_list[7].split('|')
            for gene in line_gene_list:
                if gene not in jenny:
                    jenny[gene] = []
                jenny[gene].append(line)

# Easier to strip out this index after tbh..
del jenny['.']

# Open each Park file in turn, identifying any lines of the file which overlap with the corresponding gene set
for file in files:
    with open(file, 'r') as handle:
        count = 0
        print '\n------------------------------------------\
        \nCurrent file: ', file.split('.')[0], \
        '\n------------------------------------------'
        for gene in handle:
            gene=gene.rstrip()
            if gene in jenny:
                for x in jenny[gene]:
                    print x
                    count += 1
        print 'Overlapping variants in ', file.split('.')[0], ' = ', count 


# Now import the appropriate columns from the pLI file into a dict
with open('pli.txt', 'rU') as handle:
    pli_dict = csv.DictReader(handle, delimiter='\t')
    for row in pli_dict:
        gene = row['gene']
        pli_value = float(row['pLI'])
        pli_store[gene] = pli_value

