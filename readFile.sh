#!/bin/bash
input="/home/schimar/flaxmans/bf/helico/inds_files.txt"

#while IFS= read -r var
while IFS=' ' read -r -a vars #<<< "$string"
do
	files=${vars[@]:1:1}		# array indexed from 1 and print 3 elements
	ind=${vars[0]}      #(echo $var | cut -f 1 -d ' ')

  	echo $ind 			# used for output.sam 
	echo $files			# used for file calls
done < "$input"
