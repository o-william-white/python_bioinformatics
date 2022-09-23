
import argparse
import sys
import lib.parse_fasta_fastq as parse
import lib.seq as seq
import gzip

usage = """

# at content of fasta
python fasta_fastq_at_content.py --input example.fasta 

# at content of fastq
python fasta_fastq_at_content.py --input example.fastq

# at content of fastq to output file
python fasta_fastq_at_content.py --input example.fastq --out output.txt
"""

description = """
Calculate AT content of individual sequences in a fasta or fastq file. Gzip compressed files can be used as input.
"""
# argparse
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("--input", help = "Input fasta/q file", required=True)
parser.add_argument("--out",   help = "Output file (Optional, printed to stdout by default)", required=False, type=argparse.FileType('w'), nargs="?", default=sys.stdout)
args = parser.parse_args()

# at cotent
dat = parse.read_fasta_fastq(args.input)
for record in dat:
    name, sequence = record[0], record[1]
    at_content = round(seq.at_content(sequence), 2)
    line = name + "\t" + str(at_content)
    parse.print_all(line, args.out)
    
