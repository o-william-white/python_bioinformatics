import argparse
import sys
import subprocess
import statistics
import lib.parse_fasta_fastq as parse

usage = """

# mean depth in windows of 100 bp
python samtools_depth_windows.py --input example.sam --window 100

# Notes
# Assumes only one reference - allow useage for depth across multple windows
# Create common def to identify windows
# add example sam/bam data 

"""

description = """
Calculate mean depth in windows for a sam file.
"""
# argparse
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("--input",  help = "Input sam file", required=True)
parser.add_argument("--window", help = "Window size", required=True, type=int)
parser.add_argument("--out",    help = "Output file (Optional, printed to stdout by default)", required=False, type=argparse.FileType('w'), nargs="?", default=sys.stdout)
parser.add_argument("--norm",   help = "Total number of reads to normalise coverage by", required=False, type=int)
args = parser.parse_args()

# check samtools in path
try:
    subprocess.call(["samtools"], stderr=subprocess.DEVNULL)
except FileNotFoundError:
    print("Error: samtools not in path")
    sys.exit()

# create emtpy list
depth_list = []

# samtools depth
for line in subprocess.check_output(["samtools", "depth",  "-a", args.input]).decode().split("\n"):
    line = line.rstrip("\n").split("\t")
    if len(line) == 3:
        depth_list.append(line)

# iterate through windows
for i in range(0, len(depth_list), args.window):
    start = i
    end   = i + args.window
    chunk = depth_list[start:end]
    # get mean coverage for window
    depth = [] 
    for x in chunk:
        depth.append(int(x[2]))
    m = statistics.mean(depth)
    if args.norm != None: 
        m = m / args.norm
    # print output
    out = str(start) + "\t" + str(end) + "\t" + str(m)
    parse.print_all(out, args.out)

