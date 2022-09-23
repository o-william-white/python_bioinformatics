
import argparse
import sys
import lib.parse_fasta_fastq as parse
import lib.seq as seq
import gzip

usage = """

# gc content of fasta
python fasta_fastq_gc_content.py --input example.fasta 

# gc content of fastq
python fasta_fastq_gc_content.py --input example.fastq

# gc content of fastq to output file
python fasta_fastq_gc_content.py --input example.fastq --out output.txt
"""

description = """
Calculate GC content of individual sequences in a fasta or fastq file. Gzip compressed files can be used as input.
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
    gc_content = round(seq.gc_content(sequence), 2)
    line = name + "\t" + str(gc_content)
    parse.print_all(line, args.out)
    
