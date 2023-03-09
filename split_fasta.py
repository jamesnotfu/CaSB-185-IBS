# 
# Splits a .fasta file into four smaller .fasta files of about equal length
# in order to run them through Blast online.
#
# To run, go to Terminal and make sure you are in the correct directory.
# The directory should contain both this .py file and your .fasta file.
# Then, run the following command, with 'filename' being your fasta file
# (no need to include the .fasta suffix):
#
# python3 split_fasta.py filename
#
# The four new .fasta files will be saved to your current directory. They
# will have the same name as your original file with an added suffix of
# "_1", "_2", "_3", and "_4".
#
#
# Example: If my .fasta file is named "abc.fasta" I would run:
#
# python3 split_fasta.py abc
#
# The resulting files, named "abc_1.fasta" through "abc_4.fasta", will
# be saved to the current directory.
#

import sys
import math

file_name = sys.argv[1]

with open(f'{file_name}.fasta') as f:
    data = f.read().splitlines()

index_1 = math.ceil(len(data)/4)
while data[index_1][0]!='@':
    index_1+=1
index_2 = math.ceil(2*len(data)/4)
while data[index_2][0]!='@':
    index_2+=1
index_3 = math.ceil(3*len(data)/4)
while data[index_3][0]!='@':
    index_3+=1

data_1 = data[0:index_1]
data_2 = data[index_1:index_2]
data_3 = data[index_2:index_3]
data_4 = data[index_3:len(data)]

with open(f'{file_name}_1.fasta', 'w') as new_fasta_1:
    for line in data_1:
        new_fasta_1.write(f'{line}\n')
with open(f'{file_name}_2.fasta', 'w') as new_fasta_2:
    for line in data_2:
        new_fasta_2.write(f'{line}\n')
with open(f'{file_name}_3.fasta', 'w') as new_fasta_3:
    for line in data_3:
        new_fasta_3.write(f'{line}\n')
with open(f'{file_name}_4.fasta', 'w') as new_fasta_4:
    for line in data_4:
        new_fasta_4.write(f'{line}\n')
