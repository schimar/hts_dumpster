import h5py
from os import listdir
import pandas as pd
import bz2
from re import findall

# create the file object

f = h5py.File("runs.hdf5", 'w')


#
#dset = f.create_dataset("myset", (100,), dtype= 'i')
#dset.name


# f is the root group, let's create another group (or level):
runs = f.create_group("runs")

####
# pick one folder (flaxmans/bu2s/runs/Run215500)
# listdir('.')[7]
# ls Run215500/
# listdir(listdir('.')[7])


# loop through all the directories (Run*/) and append runXXXXXX as group to root level


# then, decompress bz2 files to read them (w/ pd.read_table ?) and compress again
#decompressed = bz2.decompress(compressed)
#compressed = bz2.compress(original_data)

# e.g. runs/Run215500/..
# for the JAFSdata, create another level (group) for each Run*


#a = pd.read_table("Run215500/AlleleFreqTimeSeries.txt.bz2", sep= ' ')



rs = [listdir('.')[1], listdir('.')[3]]
# rs = listdir('.')[1:]

for i, runDir in enumerate(rs):
    files = listdir(runDir)
    for fil in files:
        if rs[i] in runs:
            continue
        else:
            runs.create_group(rs[i])
            #if findall('FST', fil):
                #tempFst = pd.read_table("FSTtimeSeries.txt")
            tmpPathFile = str(rs[i] + '/FSTtimeSeries.txt.bz2')
            tmpFile = pd.read_table(tmpPathFile, sep= ' ', header= None)
            runs[rs[i]].create_dataset("Fst", data= tmpFile.transpose())


pd.read_table(tmpPathFile, sep= ' ', header= None)


                #print rs[i], fil
            #pd.read_table(fil, sep= ' ')





runs['Run215500/'].create_dataset("Fst", data= pd.read_table("Run215500/FSTtimeSeries.txt", sep= ' '))
runs['Run215499/'].create_dataset("Fst", data= pd.read_table("Run215499/FSTtimeSeries.txt.bz2", sep= ' '))
# we need:

# Fst
# LD
# allele freqs (which?)
# for selected and non-selected sites (TS or
# NeutralAlleleFrequencies.txt
# NeutralAlleleFrequencySpectrum.csv


f.close()
f.save()



# runs.create_group('Run215500')

