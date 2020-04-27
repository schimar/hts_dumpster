samtools mpileup -uf $ref $bam.bam | bcftools view -cg - | vcfutils.pl vcf2fq | seqtk seq -A -l 70 - | sed -r "s/(>)(.*)/\1$bam.conensus/g" > $bam.consensus.fasta
