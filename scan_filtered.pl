#!/usr/bin/perl
use DDP;
use strict;

my $input_file = 'pilot_out.txt';
my $gene_file = 'genelist.txt';
my %genehash;
my $handle;
my $identified_rows = 0;
my $multi_rows = 0;

# Iterate over the gene names identified to check for instances in the hash
# Increment the values to identify the number of instances in the VCF
open($handle, '<:encoding(UTF-8)', $gene_file) 
or die "Gene file not opened!";

# Iterate over the gene list, adding entries to the row
while (my $row = <$handle>) {
    chomp $row;
    $genehash{$row} = 0;
}

# If '.' has made it as an index, delete it
if (exists($genehash{'.'})){
    delete($genehash{'.'});
}

open (my $handle2, '<:encoding(UTF-8)', $input_file)
or die "Input file not opened!";

# Load the Hash with counts of all gene symbols present in the file
# where the gene symbol is present in the gene list
my $first_line = 1;
while (my $row = <$handle2>)
{	
    # Reads each tab-separated line of the output file.  
    if ($first_line){
        $first_line = 0;
    }
    else{
        # Split on tabs to separate columns
        my @line = split(/\t/, $row);
        my @genes = split(/\,/, $line[5]);
        #for my $single_gene (@genes){
        #	print $single_gene, "\n";
        #}
        
        # For each separate symbol in that list, increase counter if found
        # rowtest examines whether a matching variant was found on that row
        my $rowtest = 0;
        # A test of whether multiple variants were caught on one line.
        my $multi_row = 0;
        for my $elem (@genes){
            if(exists($genehash{$elem})) {
                if ($rowtest){
                    $multi_row = 1;	
                }	
                $genehash{$elem}++;
                $rowtest = 1;
                print "$row \n";
            }	
        }
        # If there was a match, increment identified_rows
        if ($rowtest){
            $identified_rows++;	
        }
        if ($multi_row){
            $multi_rows++;
        }
    }	
}	
# A quick addition to identify all genes from the initial set found in the VCF,
# and to count the number of times each gene was seen. 
# This might be a little more verbose than necessary...
my $counter = 0;
my $total_instances = 0;

while(my ($gene, $value) = each %genehash) {
    if ($genehash{$gene} > 0) {
        print "Instances of $gene: $genehash{$gene}\n";
        $total_instances += $genehash{$gene};
        $counter++;
    }
}

print "$counter genes identified\n";
print "$total_instances individual gene sightings\n";
print "$identified_rows rows seen containing variants\n";
print "Multiple gene names found on $multi_rows rows\n";