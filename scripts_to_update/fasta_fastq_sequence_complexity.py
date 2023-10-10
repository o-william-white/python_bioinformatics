
import argparse
import sys
import lib.parse_fasta_fastq as parse
import lib.seq as seq
import gzip

usage = """

# sequence complexity of fasta
python fasta_fastq_sequence_complexity.py --input example.fasta 

# sequence complexity of fastq
python fasta_fastq_sequence_complexity.py --input example.fastq

# sequence complexity of fastq to output file
python fasta_fastq_sequence_complexity.py --input example.fastq --out output.txt
"""

description = """
Calculate sequence complexity of individual sequences in a fasta or fastq file. Gzip compressed files can be used as input.
"""
# argparse
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("--input", help = "Input fasta/q file", required=True)
parser.add_argument("--out",   help = "Output file (Optional, printed to stdout by default)", required=False, type=argparse.FileType('w'), nargs="?", default=sys.stdout)
args = parser.parse_args()

# gc cotent
dat = parse.read_fasta_fastq(args.input)
for record in dat:
    name, sequence = record[0], record[1]
    sequence_complexity = round(seq.sequence_complexity(sequence), 2)
    line = name + "\t" + str(sequence_complexity)
    parse.print_all(line, args.out)
    
