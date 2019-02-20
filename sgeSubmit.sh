#!/bin/bash

# Name your job. Unless you use the -o and -e options, output will
# go to a unique file name.ojob_id for each job.
#$ -N name

# Execute job in the queue "std.q" unless you have special requirements.
#$ -q std.q

# The SGE batch system uses the current directory as working directory.
# Both files (output.dat and error.dat) will be placed in the current
# directory. The batch system assumes to find the executable in this directory.
#$ -cwd

# set the number of threads
#$ -pe openmpi-12perhost


# Redirect output stream to this file.
#$ -o out.dat

# Redirect error stream to this file.
###$ -e err.dat
# join std.err to std.out 
#$ -j yes

# Send status information to this email address.
#$ -M martin.schilling@uibk.ac.at

# Send an e-mail when the job is done.
#$ -m e


./gatk.sh




## For a parallel program execute

## qsh -pe parallel-environment number-of-slots

## with the SGE's parallel environment of your choice (see the list of available parallel environments with qconf -spl) and the number of processes/threads you intend to use. This is not different from submitting a parallel job with qsub. 
## Start your parallel MPI program as depicted within the script.sh files for parallel MPI batch jobs above. For OpenMP jobs export the OMP_NUM_THREADS variable with export OMP_NUM_THREADS=$NSLOTS and start your job.


