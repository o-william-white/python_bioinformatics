
import sys
import os
from Bio import SeqIO

# run as <read_lengths.py example.fasta fasta>

# check input files specified
assert len(sys.argv) == 3, "Run as: <python read_lengths.py example.fasta fasta>"

# convert cmd line arguments to variables
file = sys.argv[1]
fmt  = sys.argv[2]

# check input file is present
assert os.path.exists(file), "Input file does not exist"

# function to preint read lengths
def read_length(file, fmt):
    for record in SeqIO.parse(file, fmt):
        print(record.name + "\t" +  str(len(record.seq)))

# run function
read_length(file, fmt)





