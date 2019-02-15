#!/bin/bash
#SBATCH -p short # Partition or queue. In this case, short!
#SBATCH --job-name=vsearch # Job name
#SBATCH --mail-type=NONE # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=schimar@gmail.COM
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=64 # Run on a single CPU
#SBATCH --mem=384gb # Memory limit
#SBATCH --time=24:00:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/masc7337/flaxmans/bf/limenitis/ekData/vsearch/slurm_%j.out # Standard output and error log
#SBATCH --error=/Users/masc7337/flaxmans/bf/limenitis/ekData/vsearch/slurm_%j.err # %j inserts job number


### Switch to the working directory; by default TORQUE launches processes
### from your home directory.
PBS_O_WORKDIR=$HOME/flaxmans/bf/limenitis/ekData/vsearch/
cd $PBS_O_WORKDIR
echo Working directory is $PBS_O_WORKDIR

### Display the job context
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
###echo Using ${NPROCS} processors across ${NNODES} nodes

### Move data from homedir / project storage to scratch - rsync will automagically verify integrity
### of all files it moves, so it is a better option than copy sometimes...
rsync -avz $HOME/flaxmans/bf/limenitis/ekData/vsearch/* /scratch/Users/masc7337/limenitis/vsearch/
### Run my python script, or whatever else IN SCRATCH
#python /scratch/Users/masc7337/jobToRun.py

### module load R/3.3.0
### source ~/.Renviron

#R --file=RfstGL.r
~/bio/vsearch-2.8.0-linux-x86_64/bin/vsearch --cluster_fast centroids.fasta --id 0.9 --threads 64 --consout 192consensus.fasta --msaout 192msa.fasta --log runInfo192cons.txt 



### MOVE MY OUTPUTS BACK TO HOMEDIR/PROJECT STORAGE
#rsync -avz /scratch/Users/masc7337/sub/fstGL/.R* $HOME/flaxmans/bf/hmel/var/subchr/sub/fstGL/
rsync -avz /scratch/Users/masc7337/limenitis/vsearch/* $HOME/flaxmans/bf/limenitis/ekData/vsearch/


