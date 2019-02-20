#!/bin/bash

WD=$1 #/scratch/c7701046/structure/test

cd $WD
PARFILEs=`ls -1 mainpar_*`

for parfile in $PARFILEs
do
	echo -e "#!/bin/bash\n\n\nstructure -m $WD/$parfile" > structure.sh
	chmod +x structure.sh
	qsub -j yes -wd $WD -N $parfile.job -l h_vmem=2G -q std.q -pe openmp 1 structure.sh

done	



  
