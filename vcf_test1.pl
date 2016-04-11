#!/usr/bin/perl
use Vcf;
use DDP;
use warnings;

my $vcf = Vcf->new(file=>'744_anno.vcf.hg19_multianno.vcf');

# unless ($vcf) {die "Input vcf not available..."}

$vcf->parse_header();

# This script will print out each entry of the VCF in full colourised DDP
# Crappy condition asking if this is what the user wants:
print "Would you like to read the full file?: (y/n)";
$this = <STDIN>;
chomp($this);
if ($this eq 'y')
{
    while (my $x=$vcf->next_data_hash())
    {
        p($x);
        # After each iteration, provide a choice to quit
        print "Press 'q' to quit, Enter to continue...";
        $quit = <STDIN>;
        chomp($quit);
        if ($quit eq "q")
        {
            exit;
        }
    }
}

# Now print some elements from the Hash
# Select one VCF row as an example
$vcf_line = $vcf->next_data_hash();

# Get Ref allele
# Only one Ref allele should exist
my $ref_element = $vcf_line->{"REF"};
print "Reference allele: $ref_element\n";

# Get Alt allele
# Nested array, to allow for multiple alternate alleles at the same locus
# Top level index is "ALT", then [0] for the first Alt allele, then [0] for the value
my @alt_element = $vcf_line->{"ALT"};
print "Variant alleme: $alt_element[0][0]\n";


# Get Position, numerical
my $pos_element = $vcf_line->{"POS"};
print "Variant position: $pos_element\n";

# Get Qual
my $qual_element = $vcf_line->{"QUAL"};
print "Quality value: $qual_element\n";

