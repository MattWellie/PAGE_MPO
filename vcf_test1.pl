#!/usr/bin/perl
use Vcf;
use DDP;

my $vcf = Vcf->new(file=>'PP0001.vcf.gz');
$vcf->parse_header();

$vcf->next_data_hash();

%vcf_hash->$vcf;
print %vcf_hash;

