
import argparse
import sys
import os

# argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fasta", help = "Input fasta file", required=True)
parser.add_argument("--out",   help = "Output directory", required=True)
args = parser.parse_args()

# tidy sequence name
def tidy_seq_name(name):
    # remove special characters
    name = name.replace('|', '_').replace(':', '').replace(',','').replace(' ', '_')
    # remove tailing full stop
    if name[-1] == '.':
        name = name[:-1]
    return(name)

# split fasta and write to files to output folder
def split_fasta(fasta, output_dir):
    # open fasta
    input_fasta = open(fasta, 'r')
    # create empty output
    output_fasta = ''
    # iterate through input
    for line in input_fasta:
        if line.startswith('>'):
            if output_fasta != '':
                output_fasta.close()
            seq_name = line[1:].rstrip('\n')
            seq_name = tidy_seq_name(seq_name)
            output_fasta = open(f'{output_dir}/{seq_name}.fasta', 'w')
            output_fasta.write(f'>{seq_name}\n')
        else:
            output_fasta.write(line)
    output_fasta.close()

# make output dir
os.mkdir(args.out)

# split fasta
split_fasta(args.fasta, args.out)

