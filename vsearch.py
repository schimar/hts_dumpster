# Working from /home/mschilling/Desktop/boechera/lasio/vsearch/


# NOTE: this is not python code! I simply used the py extension to get some juicy code highlighting here...


################ general procedure ################

# 1. parse barcodes and split fastq file by individual
# 2. cluster highly similar sequences in individual fastq files
# 3. combine the centroids from the preceding runs and cluster the entire fasta file
# 4. cluster the resulting consensus sequences at lower id (0.8) to exclude the ones that collapse (and remove all clusters with less than <threshold> (30) seqs per cluster)
# 5. align parsed reads to reference seqs (final clusters)



#############################
# 1. Splitting fastq files by individual
#############################

# perl scripts_zg/parse_barcodes768.pl bc_ms.csv gomp006_NoIndex_L005_R1_001.fastq

# perl splitFastq_ms.pl /home/mschilling/Desktop/gbs15/raw/parsed_gomp006_NoIndex_L005_R1_001.fastq /home/mschilling/Desktop/gbs15/ids.csv





#############################
# 2. Cluster highly similar sequences together within individuals (98% identity) and output the centroids:
#############################

## first, convert from fastq to fasta (see seqtk_bash in /hts_tools/)


# collapse highly similar sequences (id = 0.98) within each species:

./vsearch.sh 0.98 centroids


###########

# mv centroids* clustered_vsearch/
# mv runInfo* clustered_vsearch/

## create files with only seqs < 70

~/hts_tools/exclude_short_seqs.sh    # creates the files sub_centroids* (see bash script)
# mv sub_centroids_* subc/   (now done in the above bash script)


#############################
# 3. Combine the centroid sequences
#############################
# concatenate all fasta files into one single .fa
### NOTE: only used MS558 to MS738 (2014 lasiocarpa) for consensus seqs
cd subc/
cat *fasta > l105centroids.fasta

# 5,821,663 contigs      (grep -c \> l105_centroids.fasta)

# a) get consensus seqs for 2014 lasio samples (MS558 - MS738)
#vsearch --cluster_fast l105centroids.fasta --id 0.90 --threads 8 --consout l105_90consensus.fasta --msaout l105_90msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.91 --threads 8 --consout l105_901onsensus.fasta --msaout l105_91msa.fasta
###vsearch --cluster_fast l105centroids.fasta --id 0.92 --threads 8 --consout l105_92consensus.fasta --msaout 92l105_msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.93 --threads 8 --consout l105_93consensus.fasta --msaout l105_93msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.94 --threads 8 --consout l105_94consensus.fasta --msaout l105_94msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.95 --threads 8 --consout l105_95consensus.fasta --msaout l105_95msa.fasta

#vsearch --cluster_fast l105centroids.fasta --id 0.89 --threads 8 --consout l105_89consensus.fasta --msaout l105_89msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.88 --threads 8 --consout l105_88consensus.fasta --msaout l105_88msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.87 --threads 8 --consout l105_87consensus.fasta --msaout l105_87msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.86 --threads 8 --consout l105_86consensus.fasta --msaout l105_86msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.85 --threads 8 --consout l105_85consensus.fasta --msaout l105_85msa.fasta
#vsearch --cluster_fast l105centroids.fasta --id 0.84 --threads 8 --consout l105_84consensus.fasta --msaout l105_84msa.fasta

###

# now check different values of --id (between 90 and 95)
# (Z uses 8% and then 17% ((8*2)+1)
# (1st don't go below 90% (stay between 90 and 95)
# (2nd: centered on double the mismatch of the first and then just go up and down)

# see how many contigs I have left for each of the runs (make heatmap with thresholds for 1st and 2nd step on axes)

# to get the number of clusters for the different consensus runs (id = {90..95})
grep Clusters l105_consensus_runINF.txt > l105cons_nClust.txt

#############################
# 4. Here I am clustering the consensus sequences from 3a to see if any collapse at a lower id (80%). Any that do will be removed before moving forward.
#############################
# for every <id>consensus.fasta, run the following, with 2x the mismatch from
# the prior run

# 90 (20 +- 3)

# written to cons90/
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.77 --consout cons90/l105_90paralogs77.fasta --msaout cons90/l105_90paralogs77_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.78 --consout cons90/l105_90paralogs78.fasta --msaout cons90/l105_90paralogs78_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.79 --consout cons90/l105_90paralogs79.fasta --msaout cons90/l105_90paralogs79_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.8 --consout cons90/l105_90paralogs80.fasta --msaout cons90/l105_90paralogs80_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.81 --consout cons90/l105_90paralogs81.fasta --msaout cons90/l105_90paralogs81_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.82 --consout cons90/l105_90paralogs82.fasta --msaout cons90/l105_90paralogs82_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_90consensus.fasta --threads 10 --iddef 2 --id 0.83 --consout cons90/l105_90paralogs83.fasta --msaout cons90/l105_90paralogs83_msa.fasta --minseqlength 64

# 91 (18 +- 3)

#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.79 --consout cons91/l105_91paralogs79.fasta --msaout cons91/l105_91paralogs79_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.80 --consout cons91/l105_91paralogs80.fasta --msaout cons91/l105_91paralogs80_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.81 --consout cons91/l105_91paralogs81.fasta --msaout cons91/l105_91paralogs81_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.82 --consout cons91/l105_91paralogs82.fasta --msaout cons91/l105_91paralogs82_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.83 --consout cons91/l105_91paralogs83.fasta --msaout cons91/l105_91paralogs83_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.84 --consout cons91/l105_91paralogs84.fasta --msaout cons91/l105_91paralogs84_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_91consensus.fasta --threads 10 --iddef 2 --id 0.85 --consout cons91/l105_91paralogs85.fasta --msaout cons91/l105_91paralogs85_msa.fasta --minseqlength 64

# 92 (16 +- 3)

#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.81 --consout cons92/l105_92paralogs81.fasta --msaout cons92/l105_92paralogs81_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.82 --consout cons92/l105_92paralogs82.fasta --msaout cons92/l105_92paralogs82_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.83 --consout cons92/l105_92paralogs83.fasta --msaout cons92/l105_92paralogs83_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.84 --consout cons92/l105_92paralogs84.fasta --msaout cons92/l105_92paralogs84_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.85 --consout cons92/l105_92paralogs85.fasta --msaout cons92/l105_92paralogs85_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.86 --consout cons92/l105_92paralogs86.fasta --msaout cons92/l105_92paralogs86_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_92consensus.fasta --threads 10 --iddef 2 --id 0.87 --consout cons92/l105_92paralogs87.fasta --msaout cons92/l105_92paralogs87_msa.fasta --minseqlength 64


# 93 (14 +-3)

#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.83 --consout cons93/l105_93paralogs83.fasta --msaout cons93/l105_93paralogs83_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.84 --consout cons93/l105_93paralogs84.fasta --msaout cons93/l105_93paralogs84_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.85 --consout cons93/l105_93paralogs85.fasta --msaout cons93/l105_93paralogs85_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.86 --consout cons93/l105_93paralogs86.fasta --msaout cons93/l105_93paralogs86_msa.fasta --minseqlength 64

#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.87 --consout cons93/l105_93paralogs87.fasta --msaout cons93/l105_93paralogs87_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.88 --consout cons93/l105_93paralogs88.fasta --msaout cons93/l105_93paralogs88_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_93consensus.fasta --threads 10 --iddef 2 --id 0.89 --consout cons93/l105_93paralogs89.fasta --msaout cons93/l105_93paralogs89_msa.fasta --minseqlength 64


# 94 (12 +-3)

#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.85 --consout cons94/l105_94paralogs85.fasta --msaout cons94/l105_94paralogs85_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.86 --consout cons94/l105_94paralogs86.fasta --msaout cons94/l105_94paralogs86_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.87 --consout cons94/l105_94paralogs87.fasta --msaout cons94/l105_94paralogs87_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.88 --consout cons94/l105_94paralogs88.fasta --msaout cons94/l105_94paralogs88_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.89 --consout cons94/l105_94paralogs89.fasta --msaout cons94/l105_94paralogs89_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.90 --consout cons94/l105_94paralogs90.fasta --msaout cons94/l105_94paralogs90_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_94consensus.fasta --threads 10 --iddef 2 --id 0.91 --consout cons94/l105_94paralogs91.fasta --msaout cons94/l105_94paralogs91_msa.fasta --minseqlength 64


# 95 (10 +-3)

#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.87 --consout cons95/l105_95paralogs87.fasta --msaout cons95/l105_95paralogs87_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.88 --consout cons95/l105_95paralogs88.fasta --msaout cons95/l105_95paralogs88_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.89 --consout cons95/l105_95paralogs89.fasta --msaout cons95/l105_95paralogs89_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.90 --consout cons95/l105_95paralogs90.fasta --msaout cons95/l105_95paralogs90_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.91 --consout cons95/l105_95paralogs91.fasta --msaout cons95/l105_95paralogs91_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.92 --consout cons95/l105_95paralogs92.fasta --msaout cons95/l105_95paralogs92_msa.fasta --minseqlength 64
#vsearch --cluster_fast l105_95consensus.fasta --threads 10 --iddef 2 --id 0.93 --consout cons95/l105_95paralogs93.fasta --msaout cons95/l105_95paralogs93_msa.fasta --minseqlength 64


### now the single runs for 89 through 84 (with just (100-x)*2 as paralog id)
# 89 (22)
#vsearch --cluster_fast l105_89consensus.fasta --threads 10 --iddef 2 --id 0.78 --consout cons89_84/l105_89paralogs78.fasta --msaout cons89_84/l105_95paralogs78_msa.fasta --minseqlength 64
#
## 88 (24)
#vsearch --cluster_fast l105_88consensus.fasta --threads 10 --iddef 2 --id 0.76 --consout cons89_84/l105_88paralogs76.fasta --msaout cons89_84/l105_95paralogs76_msa.fasta --minseqlength 64
#
## 87 (26)
#vsearch --cluster_fast l105_87consensus.fasta --threads 10 --iddef 2 --id 0.74 --consout cons89_84/l105_87paralogs74.fasta --msaout cons89_84/l105_95paralogs74_msa.fasta --minseqlength 64
#
## 86 (28)
#vsearch --cluster_fast l105_86consensus.fasta --threads 10 --iddef 2 --id 0.72 --consout cons89_84/l105_86paralogs72.fasta --msaout cons89_84/l105_95paralogs72_msa.fasta --minseqlength 64
#
## 85 (30)
#vsearch --cluster_fast l105_85consensus.fasta --threads 10 --iddef 2 --id 0.70 --consout cons89_84/l105_85paralogs70.fasta --msaout cons89_84/l105_95paralogs70_msa.fasta --minseqlength 64
#
## 84 (32)
#vsearch --cluster_fast l105_84consensus.fasta --threads 10 --iddef 2 --id 0.68 --consout cons89_84/l105_84paralogs68.fasta --msaout cons89_84/l105_95paralogs68_msa.fasta --minseqlength 64




#########
# get the number of clusters from the paralog runs
# e.g.:
grep Singletons cons91/runINF.txt > cons91/sngltns79_85.txt

#~/hts_tools/get_cluster_n_of_seqs.py lasio_paralogs2.fasta lasio_paralogs2_clusters.csv

# remove the collapsed clusters (from the last vsearch run with id 0.8
/home/mschilling/Desktop/gbs15/gbs_tools_ms/remove_collapsed_clusters.py lasio_paralogs2.fasta lasio_paralogs2_seqs1.fasta # 471954 uncollapsed clusters found

# remove all clusters that have less than 30 sequences present. (no upper threshold used, since there aren't any reads with > 350

./remove_clusters_threshold.py 30 /home/mschilling/Desktop/gbs15/ind/clustered_vsearch/sub_centroids/2014/lasio_paralogs2_seqs1.fasta /home/mschilling/Desktop/gbs15/ind/clustered_vsearch/sub_centroids/2014/lasio_paralogs2_seqs1_30.fasta
# 5609 uncollapsed clusters found

#############################
# 5. I retained the subset of distinct (non-collapsed) contigs that had at least 8 reads originally. I then converted these back to fasta format and only kept contigs with consensus sequences between 72 and 92 bps in length. in all 93,134 contigs were retained.
#############################



####
# perl extractSingletons.pl

# perl noMatch2fasta.pl

# 6. A single contig with a significant blastn hit to wolbachia was dropped from the final file, leaving 93,133 contigs.


###
# first, let's clean up the fasta headers in my reference file
./clean_up_fasta_header.py /home/mschilling/Desktop/gbs15/ref/lasio_paralogs2_seqs1_30.fasta lasio_contigs.fasta

# alignment of reads to the reference (lasio_paralogs2_seqs1_50.fasta)
# in /Desktop/gbs15/ref/
bwa index lasio_contigs.fasta

# see bwa_bash and bwa_samse_bash (in /gbs_tools_ms/)

# bwa aln -t 12 -l 20 -k 2 -I -q 10 -Y -n 5 lasio_contigs.fasta parsed_gomp006_NoIndex_L005_R1_001.fastq > Blasio.sai

# bwa samse -n 1 lasio_contigs.fasta Blasio.sai parsed_gomp006_NoIndex_L005_R1_001.fastq > Blasio.sam

# convert sam to bam
samtools view -S -u Blasio.sam -o Blasio.bam

# samtools sort Blasio.sam Blasio.sorted
# samtools index Blasio.sorted.bam

############


# now I'll take the l105_88consensus.fasta and align it to the Bstricta assembly

~/bwa/bwa index l105_88consensus.fasta

#~/bwa/bwa aln -t 10 -l 20 -k 2 -q 10 -Y -n 5 ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa l105_88consensus.fasta -f aln/l105_88stricta.sai

#~/bwa/bwa samse -n 1 /home/mschilling/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa aln/l105_88stricta.sai l105_88consensus.fasta -f aln/l105_88stricta.sam

#samtools view -S -u -h aln/l105_88stricta.sam -o aln/l105_88stricta.bam


#samtools flagstat aln/l105_88stricta.bam
# 700972 + 0 in total (QC-passed reads + QC-failed reads)
# 0 + 0 duplicates
# 135044 + 0 mapped (19.27%:-nan%)

#########
### try bwa mem
#~/bwa/bwa mem -t 10 -Y -a -C ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa l105_88consensus.fasta > aln/l105_88strictaMEM.sam
#samtools view -bS aln/l105_88strictaMEM.sam > aln/l105_88strictaMEM.bam
#samtools flagstat aln/l105_88strictaMEM.bam
#1669459 + 0 in total (QC-passed reads + QC-failed reads)
#0 + 0 duplicates
#1359084 + 0 mapped (81.41%:-nan%)

######################
# strictaMEM2   (in /select/stricta_aln/mem/)
~/bwa/bwa index ../l105_88consensus.fasta



~/bwa/bwa mem -t 10 -w 50 -k 20 -a -C ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa ../l105_88consensus.fasta > l105_88strictaMEM2.sam

~/x_app/samtools/samtools view -h -bS l105_88strictaMEM2.sam > l105_88strictaMEM2h.bam
~/x_app/samtools/samtools flagstat l105_88strictaMEM2.bam
# 1621949 + 0 in total (QC-passed reads + QC-failed reads)
# 893454 + 0 secondary
# 27523 + 0 supplementary
# 0 + 0 duplicates
# 1300497 + 0 mapped (80.18%:-nan%)



#
~/x_app/samtools/samtools sort l105_88strictaMEM2.bam -o l105_88strictaMEM2.sorted

~/x_app/samtools/samtools depth l105_88strictaMEM2.sorted.bam > l105_88strictaMEM2.depth

# extract all unmapped segments (see 'samtools flag' in manual)
# ~/x_app/samtools/samtools view -f4 l105_88strictaMEM2.bam > l105_88MEM2unmapped.txt
# ./samtools_f4tofasta l105_88MEM2unmapped.txt > l105_88MEM2unmpd.fasta



# now get the fasta from the actual alignment (bam)
~/x_app/samtools/samtools fasta l105_88strictaMEM2.sorted.bam > l105_88strictaMEM2.fasta

# then combine alignment with unmapped fasta

# cat *.fasta > l105_88strictaMpd_Unmpd.fasta

#~/hts_tools/exclude_short_seqs.py l105_88strictaMpd_Unmpd.fasta l105_88strictaMpd_Unmpd_shortexcl.fasta

# vsearch, cluster at low id, to see how many collapse.
vsearch --cluster_fast l105_88strictaMEM2.fasta --threads 10 --iddef 2 --id 0.76 --consout l105_88strictaMEM2Paralogs76.fasta --msaout l105_88strictaMEM2Paralogs76_msa.fasta --minseqlength 64

# MEM2
# 59420106 nt in 691094 seqs, min 64, max 97, avg 86
# WARNING: 9878 sequences shorter than 64 nucleotides discarded.
# Masking 100%
# Sorting by length 100%
# Counting unique k-mers 100%
# Clustering 100%
# Sorting clusters 100%
# Writing clusters 100%
############################################# Clusters: 495815 Size min 1, max 1132, avg 1.4
# Singletons: 415813, 60.2% of seqs, 83.9% of clusters
# Multiple alignments 100%

### compared to the aln/samse version: 114247 uncollapsed clusters found

## now with both mapped and unmapped reads:

# vsearch --cluster_fast l105_88MEM2AllRds.fasta --threads 8 --iddef 2 --id 0.76 --consout l105_88MEM2AllRdsPara76.fasta --msaout l105_88MEM2AllRdsPara76msa.fasta --minseqlength 64
# 80501611 nt in 935218 seqs, min 64, max 97, avg 86
# WARNING: 15429 sequences shorter than 64 nucleotides discarded.
# Masking 100%
# Sorting by length 100%
# Counting unique k-mers 100%
# Clustering 100%
# Sorting clusters 100%
# Writing clusters 100%
############################################# Clusters: 498835 Size min 1, max 1598, avg 1.9
# Singletons: 259318, 27.7% of seqs, 52.0% of clusters


# extract singletons
~/hts_tools/remove_collapsed_clusters.py l105_88strictaMEM2Paralogs76.fasta l105_88strictaMEM2Consensus76.fasta
# MEM2: 415813 uncollapsed clusters found

# check for duplicate headers
grep '>' l105_88strictaMEM2Consensus76.fasta | sort | uniq -c > outfuniq.txt


~/hts_tools/remove_clusters_threshold.py 10 l105_88strictaMEM2Consensus76.fasta l105_88strictaMEM2Cons76_10.fasta
# with 10: 19348 uncollapsed clusters fou
# with 5:  39482 uncollapsed clusters found    <--- used this one

#~/hts_tools/get_cluster_n_of_seqs.py para l105_88strictaParalogs76.fasta l105_88strictaParalogs76_nClust.txt
java -jar ~/x_app/picard/build/libs/picard.jar CreateSequenceDictionary REFERENCE=l105_88strictaMEM2Cons76_5hdr_clnd.fasta OUTPUT=l105_88strictaMEM2Cons76_5hdr_clnd.dict
~/x_app/samtools/samtools faidx l105_88strictaMEM2Cons76_5hdr_clnd.fasta

# now align all 105 lasio
~/bwa/bwa index l105_88strictaMEM2Cons76_5hdr_clnd.fasta

#~/bwa/bwa mem         #  l105_88strictaMEM2Cons76_10.fasta
~/hts_tools/bwa_mem   # with l105_88strictaMEM2Cons76_10.fasta
~/hts_tools/sam2bam_bash

~/hts_tools/samtools_sort
~/hts_tools/samtools_indx
# MEM2 all reads (mapped and unmapped)
# for MEM2AllRdsPara76.fasta: remove_collapsed... : 259318 uncollapsed clusters found (MEM2AllRdsCons76.fasta)
# remove_clusters_threshold.py:
    #   5: 35269 uncollapsed clusters found

# align l105 to consensus
#./bwa_aln

#./bwa_samse
# call variants

# use depth to filter out variants that have depth >= 2

# get centroidID and scafbp pos (see script; but this has also been built into the bwaDepthFilter.py)
~/hts_tools/extr_centr_scafbp_samf.py l105_88strictaMEM2.sam > l105_88strictaMEM2centroidID_scafbp.txt


# run bwaDepthFilter.py (with depth == 1)
~/hts_tools/bwaDepthFilterClust.py l105_88strictaMEM2Cons76_5.vcf l105_88strictaMEM2.depth l105_88strictaMEM2.sam > outfClust.vcf



# GATK run with lasio aligned to stricta (with bwa mem)
java -jar /home/mschilling/gatk/GenomeAnalysisTK.jar -T UnifiedGenotyper -R ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa -I lasio105.list -o lasio105strictaMEM.vcf -nct 20 -glm SNP -hets 0.001 -mbq 20 -ploidy 2 -stand_call_conf 50 -maxAltAlleles 2 -writeFullFormat



###########################################   mpileup

# sort bam file according to genomic position (not very meaningful, but mpileup only takes this, not sorted by name) and index it
samtools sort Blasio.bam Blasio.sorted
samtools index Blasio.sorted.bam

# samtools mpileup
samtools mpileup -u -E -D -C 50 -g -I -q 10 -Q 15 -f lasio_contigs.fasta Blasio.sorted.bam > blasio_variants.bcf

# bcftools

bcftools view -e -g -c -v -N -d 0.3 -p 0.01 -t 0.001 *variants.bcf > blasio_variants_d30.vcf

##################
bcftools view -e -g -c -v -N -d 0.8 -p 0.01 -t 0.001 blasio_variants.bcf > blasio_variants_d80.vcf # 2490 8134

bcftools view -e -g -c -v -N -d 0.3 -p 0.01 -t 0.001 blasio_variants.bcf > blasio_variants_d30.vcf



####
bcftools view -e -c -v -N -d 0.8 -p 0.01 -t 0.001 blasio_variants.bcf > blasio_variants_d80.vcf # that gives me 2570 SNVs, let's try to use

# -d 0.3 (have to be present in 30% or the individuals.
bcftools view -e -c -v -N -d 0.3 -p 0.01 -t 0.001 blasio_variants.bcf > blasio_variants_d30.vcf # same as above (2570), so let's try:

# -p 0.1
bcftools view -e -c -v -N -d 0.3 -p 0.1 -t 0.001 blasio_variants.bcf > blasio_variants_d30_p0.1.vcf # 3003

# -p 0.4
bcftools view -e -c -v -N -d 0.3 -p 0.4 -t 0.001 blasio_variants.bcf > blasio_variants_d30_p0.4.vcf # 3624

