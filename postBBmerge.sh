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

	cd ../

done

#unset IFS

