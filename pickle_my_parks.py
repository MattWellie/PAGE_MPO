"""
    
This script will find files prefixed with 'park_', which represent gene lists    
The gene lists will then be read into a dictionary, indexed by their file name

The dictionary will be pickled as 'pickled_park.cPickle' (not park prefixed to 
prevent some future errors)
"""

import cPickle, os

files = [file for file in os.listdir('.') if file.split('_')[0] == 'park']

outdict = {}

for file in files:
    with open(file, 'r') as handle:
        outdict[file] = set()
        for gene in handle:
            gene=gene.rstrip()
            outdict[file].add(gene)

with open('pickled_park.cPickle', 'wb') as handle:
    cPickle.dump(outdict, handle)