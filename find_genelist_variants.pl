#!/usr/bin/perl
use Vcf;
use DDP;
use strict;

my $vcf_file = 'PP0001.vcf.gz';
my $gene_file = 'genelist.txt';
my %genehash;
my $handle;
my $identified_rows = 0;
my $multi_rows = 0;

my $vcf = Vcf->new(file=>$vcf_file);
my $header = $vcf->parse_header();

# Iterate over the gene names identified to check for instances in the hash
# Increment the values to identify the number of instances in the VCF
open($handle, '<:encoding(UTF-8)', $gene_file) 
	or die "Gene file not opened!";

# Iterate over the 
while (my $row = <$handle>) {
	chomp $row;
	$genehash{$row} = 0;
}

# Load the Hash with counts of all gene symbols present in the file
# where the gene symbol is present in the gene list
while (my $row=$vcf->next_data_hash())
{	
	# This takes the "SYMBOL=FOO|BAR" annotation and splits on "|"
	# to create the list of all separate symbols
	my @gene_list = split(/\|/, $row->{"INFO"}{"SYMBOL"});
	
	# For each separate symbol in that list, increase counter if found
	# rowtest examines whether a matching variant was found on that row
	my $rowtest = 0;
	# A test of whether multiple variants were caught on one line.
	my $multi_row = 0;
	foreach my $elem (@gene_list){
		if(exists($genehash{$elem}) && $elem ne ".") {
			if ($rowtest){
				$multi_row = 1;	
			}	
			$genehash{$elem}++;
			$rowtest = 1;
		}	
	}
	# If there was a match, increment identified_rows
	if ($rowtest){
		$identified_rows++;	
	}
	if ($multi_row){
		$multi_rows++
	}
}	

# A quick addition to identify all genes from the initial set found in the VCF,
# and to count the number of times each gene was seen. 
# This might be a little more verbose than necessary...
my $counter = 0;
my $total_instances = 0;

while(my ($gene, $value) = each %genehash) {
	if ($genehash{$gene} > 0) {
		# print "Instances of $gene: $genehash{$gene}\n";
		$total_instances += $genehash{$gene};
		$counter++;
	}
}

print "$counter genes identified\n";
print "$total_instances individual gene sightings\n";
print "$identified_rows rows seen containing variants\n";
print "Multiple gene names found on $multi_rows rows\n";
