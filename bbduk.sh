#! /bin/bash 

# Read through a list of PE seq files and use bbduk to perform quality trimming, adapter trimming, and to create histograms (base composition, quality and length distribution) 

p1=( 41*R1*.fastq.gz )
p2=( 41*R2*.fastq.gz )

for i in {0..84}; do 
	flstm=$(echo ${p1[$i]} | cut -f1,2,3,4,5,6 -d'_' | sort | uniq )
	echo $flstm
	~/bio/bbmap/bbduk.sh -Xmx1g in1=${p1[$i]} in2=${p2[$i]} out1=${flstm}_R1_001.trmd.fq out2=${flstm}_R2_001.trmd.fq ref=../../shd/adapters.fa ktrim=r k=23 mink=11 hdist=1 bhist=hist/${flstm}.bhist qhist=hist/${flstm}.qhist lhist=hist/${flstm}.lhist &> log/${flstm}.log tpe tbo 
done



