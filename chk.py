#! /usr/bin/python


# This scripts reads a vcf file and a file with individuals to be selected (one sample id per line).
# The output is a vcf file with only the selected individuals.
#
# Usage: ./sub_vcf.py <vcf_file> <select ids file> > outfile.vcf


from sys import argv
import re
import os


ls = os.listdir(argv[2])

#print ls[0]
#print re.findall('fq.gz', ls)

idict = dict()
with open(argv[1], 'rb') as ids:
    for id in ids:
        line = id.split('\n')[0].split('\t')
        if not line[0] in idict:
            idict[line[0]] = [line[1]]
        else:
            idict[line[0]].append(line[1])


for key, value in idict.iteritems():
    print key, ' '.join(value) #key, value, len(value)

#print idict[line[0]]


#with open(sys.argv[1], 'rb') as file:
#    ix_list = list()
#    select_inds = list()
#    for line in file:
#        new_line = list()
#        if line[0:2] == '##':
#            print line.split('\n')[0]
#            continue
#        elif line[0:2] == '#C':
#            #print line.split('\n')[0]
#            line_list = line.split('\t')
#            vcf_inds = line_list[9:len(line_list)]
#            last_ind = vcf_inds[-1].split('\n')[0]
#            vcf_inds[-1] = last_ind
#            new_line = line_list[0:9]
#            for j, ind in enumerate(vcf_inds):
#                if ind in ind_list:
#                    ix_list.append(j+9)
#                    new_line.append(line_list[j+9])
#                last_ind = new_line[-1].split('\n')[0]
#                new_line[-1] = last_ind
#            #print new_line
#        else:
#            line_list = line.split('\t')
#            new_line = line_list[0:9]
#            for ix in ix_list:
#                new_line.append(line_list[ix])
#            last_ind = new_line[-1].split('\n')[0]
#            new_line[-1] = last_ind
#        print '\t'.join(new_line)
#
#    file.close()

