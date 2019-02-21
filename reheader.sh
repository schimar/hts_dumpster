#! /bin/bash

input="/media/schimar/schimar2/bf/MZH11020_Butterfly_re-sequencing/sample_lib.txt"

while IFS=' ' read -r -a vars #<<< "$string"
do
	#files=${vars[@]:1:1}	
	#ind=${vars[0]}
	
	ind=$(echo $vars | cut -f 1 -d ' ')
	file=$(echo $vars | cut -f 2 -d ' ')
	files=$(ls ${file}*)
	#farray=()
	for j in $files; do
		fp=$(echo $j | cut -f 1 -d.)
		echo $ind
		echo $j
		#echo $fp
		#echo "s/SM:$fp/SM:$ind/g"
		samtools view -H $j | sed -e "s/SM:$fp/SM:$ind/g" | samtools reheader - $j > /media/schimar/butterfly/schimar/bf/hmel/aln/$j
	done
	
#

#for i in *.bam; do
#    file=$(echo $i | cut -f9 -d/)
#    id=$(echo $file | cut -f1 -d.)
#    #id=$(echo $id | cut -f7 -d/)
#    RG=${variable}'@RG:\tID:'${id}
#	echo $i

done < "$input"


#for i in *.bam; do
#	echo $i
#
#done



