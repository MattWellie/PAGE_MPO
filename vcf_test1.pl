#!/usr/bin/perl
use Vcf;
use DDP;

my $vcf = Vcf->new(file=>'PP0001.vcf.gz');
$vcf->parse_header();

while (my $x=$vcf->next_data_hash()) 
    {
	p($x);
	$this = <STDIN>;
    }
