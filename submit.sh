#!/bin/bash
#SBATCH -p short # Partition or queue. In this case, short!
#SBATCH --job-name=slurm_test # Job name
#SBATCH --mail-type=NONE # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=YOU@YOUREMAIL.COM
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=1gb # Memory limit
#SBATCH --time=00:20:00 # Time limit hrs:min:sec
#SBATCH --output=/Users/YOU/slurm_test_%j.out # Standard output and error log
#SBATCH --error=/Users/YOU/slurm_test_%j.err # %j inserts job number
