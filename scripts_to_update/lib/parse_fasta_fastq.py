
import argparse
import gzip
from io import TextIOWrapper

# open normal or .gz text file
def open_all(filename):
    if filename.endswith(".gz"):
        return gzip.open(filename, "rt")
    else:
        return open(filename, "r")

# read fasta
def read_fasta(filename):
    name, seq = None,""
    fasta = open_all(filename)
    for line in fasta:
        if line.startswith('>') and name == None:
            name = line.rstrip('\n').replace('>','')
        else:
            if line.startswith('>') and name != None:
                yield [name, seq]
                name = line.rstrip('\n').replace('>','')
                seq = ''
            else:
                seq = seq + line.rstrip('\n')
    yield [name, seq]
    fasta.close()

# check fasta
fasta_endings = (".fasta", ".fasta.gz", ".fa", ".fa.gz")
def check_fasta(filename):
    if not filename.endswith(fasta_endings):
        raise argparse.ArgumentTypeError("Input fasta file must end with any of the following: " + " ".join(fasta_endings))
    fasta = open_all(filename)
    first_line = fasta.readline()
    if not first_line.startswith(">"):
        raise argparse.ArgumentTypeError("Input does not look like a fasta, the first line should start with '>'")
    fasta.close()
    return filename

# read fastq
# only yields name and sequences by default so it can use the same functions for fasta files
def read_fastq(filename):#, include_qual=False):
    fastq = open_all(filename)
    for line in fastq:
        if line.startswith("@"):
            name = line.rstrip("\n")
            seq = fastq.readline().rstrip("\n")
            if fastq.readline().startswith("+"):
                qual = fastq.readline().rstrip("\n")
                yield [name, seq, qual]
    fastq.close()

# check fastq
fastq_endings = (".fastq", ".fastq.gz", ".fq", ".fq.gz")
def check_fastq(filename):
    if not filename.endswith(fastq_endings):
        raise argparse.ArgumentTypeError("Input fastq file must end with any of the following: " + " ".join(fastq_endings))
    fastq = open_all(filename)
    first_line = fastq.readline()
    if not first_line.startswith("@"):
        raise argparse.ArgumentTypeError("Input does not look like a fastq, the first line should start with '@'")
    fastq.close()
    return filename

# read fasta or fastq
def read_fasta_fastq(filename):
    if filename.endswith(fasta_endings):
        return read_fasta(filename)
    else:
        if filename.endswith(fastq_endings):
            return read_fastq(filename)
        else:
            raise argparse.ArgumentTypeError("Input must end with any of the following: " + " ".join(fasta_endings) + " ".join(fastq_endings))

# print line to output
def print_all(text, filename):
    if isinstance(filename, TextIOWrapper) and filename.name.endswith(".gz"):
        with gzip.open(filename.name, "at") as output:
            output.write(text + "\n")
    else: 
        print(text, file = filename)

