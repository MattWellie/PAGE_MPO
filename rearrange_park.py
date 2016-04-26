import os, cPickle

genelist = 'genes_of_interest.cPickle'
all_genes = set()
files = [file for file in os.listdir('.') if file.split('_')[0] == 'park']

with open(genelist, 'r') as handle:
    known = cPickle.load(handle)

for file in files:
    with open(file, 'r') as inhandle:
        count = 0
        for line in inhandle:
            gene = line.rstrip()
            all_genes.add(gene)
            if gene in known:
                count += 1
        print 'Known genes in {} = {}'.format(file.split('.')[0], count)


print 'The Park set contains ', len(all_genes), ' unique genes'

count = 0
for gene in all_genes:
    if gene in known:
        count+=1

print count, ' of these are previously seen'