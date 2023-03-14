import argparse
import sys
import lib.parse_fasta_fastq as parse
import lib.seq as seq
import gzip

usage = """

# rename fasta sequences s1 to sn
python fasta_rename.py --input example.fasta --prefix seq 

"""

description = """
Rename fasta sequences <prefix>1 to <prefix>n. Gzip compressed files can be used as input.
"""
# argparse
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("--input",  help = "Input fasta file", required=True)
parser.add_argument("--prefix", help = "Prefix to for sequence names", required=True)
parser.add_argument("--out",    help = "Output file (Optional, printed to stdout by default)", required=False, type=argparse.FileType('w'), nargs="?", default=sys.stdout)
args = parser.parse_args()

# gc cotent
dat = parse.read_fasta(args.input)
i = 1
for record in dat:
    name, sequence = record[0], record[1]
    new_name = args.prefix + str(i)
    line = ">" + new_name + "\n" + sequence
    parse.print_all(line, args.out)
    i += 1

