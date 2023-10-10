import argparse
import sys
import lib.parse_fasta_fastq as parse
import lib.seq as seq
import gzip

usage = """

# N content of fasta in windows of 100 bp
python fasta_n_content_windows.py --input example.fasta --window 100

"""

description = """
Calculate N content in windows for individual sequences in a fasta. Gzip compressed files can be used as input.
"""
# argparse
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("--input",  help = "Input fasta file", required=True)
parser.add_argument("--window", help = "Window size", required=True, type=int)
parser.add_argument("--out",    help = "Output file (Optional, printed to stdout by default)", required=False, type=argparse.FileType('w'), nargs="?", default=sys.stdout)
args = parser.parse_args()

# gc cotent
dat = parse.read_fasta(args.input)
for record in dat:
    name, sequence = record[0], record[1]
    for i in range(0, len(sequence), args.window):
        start = i
        end   = i + args.window
        chunk = sequence[start:end]
        n_content = round(seq.n_content(chunk), 2)
        line = name + "\t" + str(start) + "\t" + str(end) + "\t" + str(n_content)
        parse.print_all(line, args.out)
