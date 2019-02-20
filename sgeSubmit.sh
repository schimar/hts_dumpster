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

# Redirect output stream to this file.
#$ -o out.dat

# Redirect error stream to this file.
#$ -e err.dat

# Send status information to this email address.
#$ -M martin.schilling@uibk.ac.at

# Send an e-mail when the job is done.
#$ -m e

# For example an additional script file to be executed in the current
# working directory. In such a case assure that script.sh has 
# execute permission (chmod +x script.sh).
./script.sh
