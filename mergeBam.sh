#!/bin/bash
input="/media/schimar/schimar2/bf/MZH11020_Butterfly_re-sequencing/inds_files.txt"

#while IFS= read -r var
while IFS=' ' read -r -a vars #<<< "$string"
do
	files=${vars[@]:1:3}		# array indexed from 1 and print 3 elements
	ind=${vars[0]}      #(echo $var | cut -f 1 -d ' ')

  	echo ${ind}.bam 			# used for output.sam 
	#echo $files			# used for file calls
	samtools merge ${ind}.bam $files
done < "$input"
