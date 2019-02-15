#! /bin/bash

# this script comes after bbmerge.sh, to add lane & merge/unmerged to the headers and then cat all fq files. 

shopt -s nullglob

#IFS=$'
#'

#$array = (dir *.txt).
for i in 433*/; do 

	cd $i
	echo $i
	fqs1m=$( dir *l1m.fq )
	fqs1um=$( dir *l1um.fq )
	fqs2m=$( dir *l2m.fq )
	fqs2um=$( dir *l2um.fq )
	#id=$( echo $fqs1m | cut -f1 -d$'.' )
	declare -a fqs=( $fqs1m $fqs1um $fqs2m $fqs2um )
	echo ${fqs[@]}
	# change headers to ID_laneX<merged|unmerged>
	for j in ${fqs[@]}; do
		id=$( echo $j | cut -f1 -d$'.' )
		sed -i "/^@SEQILMN03/ s/$/ $id/" $j
	done
	# cat all fqs into one
	ID=$( echo $fqs1m | cut -f1 -d$'_' )
	cat ${fqs[@]} > $ID.fq

	

#	lane1=( *L001*.fastq.gz )
#	lane2=( *L002*.fastq.gz )
#	fileN1R1=$( echo ${lane1[0]} | cut -f1 -d'.' )
#	fileN1R2=$( echo ${lane1[1]} | cut -f1 -d'.' )
#	fileN2R1=$( echo ${lane2[0]} | cut -f1 -d'.' )
#	fileN2R2=$( echo ${lane2[1]} | cut -f1 -d'.' )
#
#	gunzip -f -c ${lane1[0]} > ${fileN1R1}.fq
#	gunzip -f -c ${lane1[1]} > ${fileN1R2}.fq
#	gunzip -f -c ${lane2[0]} > ${fileN2R1}.fq
#	gunzip -f -c ${lane2[1]} > ${fileN2R2}.fq
#
#	id1=$(echo ${lane1[0]} | cut -f2 -d'_')
#	id2=$(echo ${lane2[0]} | cut -f2 -d'_')
#	#
#	~/bio/bbmap/bbmerge.sh in=${fileN1R1}.fq in2=${fileN1R2}.fq -out=${id1}_l1m.fq -outu=${id1}_l1um.fq ihist=${id1}_hist1.txt
#	~/bio/bbmap/bbmerge.sh in=${fileN2R1}.fq in2=${fileN2R2}.fq -out=${id2}_l2m.fq -outu=${id2}_l2um.fq ihist=${id2}_hist2.txt
	#gzip *fastq.gz

	#rm ${fileN1R1}.fq ${fileN1R2}.fq ${fileN2R1}.fq ${fileN2R2}.fq

	cd ../

done

#unset IFS

