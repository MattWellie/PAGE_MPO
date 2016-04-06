import cPickle
import numpy as np
import matplotlib.pyplot as plt

"""
Hacky hacky hack, to show the HI scores of all DDG2P genes for reference
"""


# Import and use the pickled set of annotations from the DDD project
# This contains the HI, HS, and phenotype details where available
with open('annotations.cPickle', 'r') as handle:
    anno_dict = cPickle.load(handle)

# Then find all the HI scores present:		
# Create a list to hold all the 
hi_scores = []
for chromosome in anno_dict:
    for gene in anno_dict[chromosome]:
        ann_keys = anno_dict[chromosome][gene].keys()
        if 'hi_score' in ann_keys: 
            hi_scores.append(float(anno_dict[chromosome][gene]['hi_score']))
            
# Plot this as a graph            
line = plt.figure()
plt.plot(sorted(hi_scores), 'o')
plt.ylabel('HI Score')
plt.xlabel('Gene (sorted by HI score)')
plt.title('A scatter plot of all the HI scores affiliated with the mouse-lethal associated genes')
plt.show()