#!/usr/bin/perl
use Vcf;
use DDP;

my $vcf = Vcf->new(file=>'PP0001.vcf.gz');
$vcf->parse_header();

<<<<<<< HEAD
$vcf->next_data_hash();

%vcf_hash->$vcf;
print %vcf_hash;

=======
$line = $vcf->next_data_hash();

my %vcf_hash = %{$line}; # This works
p(%vcf_hash);

my $vcf_pos = $line->{"POS"};
print "POS = $vcf_pos \n";

my $vcf_ref = $line->{"REF"};
print "REF = $vcf_ref \n";

my $vcf_2deep = $line->{"INFO"}{"AC"};
print "AC = $vcf_2deep \n";

my $vcf_3deep = $line->{"gtypes"}{"PP0001"}{"AD"};
print "genotypes-sample-AD = $vcf_3deep \n";
>>>>>>> db0605bd87922bed98a549326eb2d0004d69ca4d
