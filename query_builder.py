# Script to build queries based on results from variants passing filters

in_file = 'summary.txt'
template = 'zgrep {} /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/{}/{}/{}/vcf/{}.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep {}'

with open(in_file, 'r') as handle:
    for line in handle:
        list = line.split('\t')
        if list[0] = 'proband': continue
        else:
            PP = list[0]
            pp1 = PP[:2]
            pp2 = PP[2:]
            pos = list[4]
            gene = list[5]
            
            print template.format(gene, pp1, pp2, PP, PP, pos)
    
"""
    Results are:
    
    zgrep LAMA5 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/00/04/PP0004/vcf/PP0004.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 60886088
    zgrep LAMA5 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/00/04/PP0004/vcf/PP0004.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 60892813
    zgrep ATP6V1B2 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/00/25/PP0025/vcf/PP0025.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 20069263
    zgrep AGAP1 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/00/65/PP0065/vcf/PP0065.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 236839424
    zgrep DNAJC16 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/67/PP0267/vcf/PP0267.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 15894604
    zgrep CLSPN /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/67/PP0267/vcf/PP0267.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 36216977
    zgrep DHX33 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/67/PP0267/vcf/PP0267.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 5365725
    zgrep SCN4A /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/03/15/PP0315/vcf/PP0315.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 62022122
    zgrep KIF26B /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/73/PP0273/vcf/PP0273.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 245766015
    zgrep KIF26B /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/73/PP0273/vcf/PP0273.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 245851740
    zgrep RP11-445F12.2,RNA5SP439,SYNRG,C17orf78,CTC-268N12.3,RP11-445F12.1,CTD-3194G12.1,CTD-3194G12.2,LHX1,DDX52,TADA2A,RP11-378E13.4,HNF1B,HMGB1P24,RP11-697E22.1,RP11-697E22.3,RP11-697E22.2,CTC-421K24.1,CTB-75G16.1,ZNHIT3,MRM1,ACACA,CTB-75G16.3,MIR2909,DHRS11,YWHAEP7,RP11-378E13.3,CTC-268N12.2,PIGW,DUSP14,RP11-333J10.2,RP11-333J10.3,RP11-19G24.2,RP11-19G24.1,AATF,MYO19,AC091199.1,RP11-115K3.1,GGNBP2 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/70/PP0270/vcf/PP0270.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 34842342
    zgrep RP11-445F12.2,RNA5SP439,SYNRG,C17orf78,CTC-268N12.3,RP11-445F12.1,CTD-3194G12.1,CTD-3194G12.2,LHX1,DDX52,TADA2A,RP11-378E13.4,HNF1B,HMGB1P24,RP11-697E22.1,RP11-697E22.3,RP11-697E22.2,CTC-421K24.1,CTB-75G16.1,ZNHIT3,MRM1,ACACA,CTB-75G16.3,MIR2909,DHRS11,YWHAEP7,RP11-378E13.3,CTC-268N12.2,PIGW,DUSP14,RP11-333J10.2,RP11-333J10.3,RP11-19G24.2,RP11-19G24.1,AATF,MYO19,AC091199.1,RP11-115K3.1,GGNBP2 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/70/PP0270/vcf/PP0270.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 34842342
    zgrep TSSK1A,LINC00896,CRKL,KRT18P62,DGCR9,DGCR8,SLC9A3P2,BCRP5,RNU6-225P,XXbac-B444P24.14,TMEM191A,DGCR5,XXbac-B444P24.13,XXbac-B444P24.10,DGCR6,XXbac-B135H6.18,AC000067.1,RTN4R,XXbac-B135H6.15,GSC2,Y_RNA,SLC25A1,AC007731.1,MIR1286,SNAP29,AC006547.13,SMPD4P1,MRPL40,LZTR1,SLC7A4,MIR3618,AC000078.5,TANGO2,AC000081.2,SEPT5,CA15P1,CA15P2,AC002472.1,RNY1P9,POM121L4P,AC007050.18,USP41,AC000095.9,XXbac-B33L19.10,DGCR6L,ZNF74,AC007050.1,AC006547.14,AC006547.15,TXNRD2,CLDN5,GGTLC3,AC004471.10,AC000068.10,MIR4761,CDC45,RN7SL168P,SNORA77,MIR1306,SERPIND1,ZDHHC8,PRODH,C22orf29,TUBA3FP,AIFM3,ABHD17AP4,DGCR2,PI4KA,AC007326.9,KRT18P5,TBX1,FAM230A,P2RX6P,AC000077.2,RN7SL812P,XXbac-B33L19.4,XXbac-B33L19.6,XXbac-B33L19.3,GP1BB,AC007308.6,AC007308.7,C22orf39,RANBP1,PI4KAP1,TSSK2,ARVCF,MIR185,AC007050.17,COMT,AC004461.4,AC011718.2,AC011718.3,AC011718.1,SCARF2,HIRA,AC023490.1,AC023490.2,SCARNA17,AC002472.11,AC006547.8,AC002472.13,SCARNA18,RN7SL389P,GNB1L,AC000068.9,TRMT2A,RN7SKP131,AC000068.5,KLHL22,RIMBP3,SNORA15,AC004463.6,MED15,P2RX6,AC004471.9,snoU13,MIR649,CLTCL1,XXbac-B444P24.8,THAP7-AS1,XXbac-B562F10.11,THAP7,AC000089.3,DGCR11,DGCR10,DGCR14,PPP1R26P2,PPP1R26P3,UFD1L /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/02/25/PP0225/vcf/PP0225.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 18893860
    zgrep CHRNA1 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/03/03/PP0303/vcf/PP0303.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 175614789
    zgrep CHRNA1 /lustre/scratch115/realdata/mdt3/projects/pagedata/data_freezes/2015-09-03/PP/03/03/PP0303/vcf/PP0303.uber_vep_tabix_qc.2015-11-11.vcf.gz | grep 175619069
"""
        