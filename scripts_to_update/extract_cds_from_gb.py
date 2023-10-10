
import argparse
from Bio import SeqIO

# argument parser
parser = argparse.ArgumentParser(description='Extract fasta of CDS sequences from genbank file')
parser.add_argument('-gb', metavar='genbank_file', help='Input genbank file',                        type=str, required=True)
parser.add_argument('-o',  metavar='output',       help='Output',                                    type=str, required=True)
parser.add_argument('-g',  metavar='gene(s)',      help='Comma separated list of genes to extract',  type=str, required=False)
args = parser.parse_args()

# read input gb 
record = SeqIO.read(args.gb, 'gb')

# set up empty list
gene_list = []

# loop through sequence feature and append genes to list
for feature in record.features:
    if feature.type == 'CDS' and 'gene' in feature.qualifiers.keys():
        # get gene name
        gene_name = feature.qualifiers['gene'][0]
        # get gene sequence
        gene_seq = feature.extract(record)
        # edit sequence name and description
        gene_seq.id = gene_name
        gene_seq.description = ''
        # append gene to genelist
        gene_list.append(gene_seq)
        
# if not target genes specified, write all to fasta
if args.g == None:
    SeqIO.write(gene_list, args.o, "fasta")
else:
    # if target genes specified, append to target_genes and write to fasta
    target_genes = []
    for gene in gene_list:
        if gene.id in args.g.split(","):
            target_genes.append(gene)        
    SeqIO.write(target_genes, args.o, "fasta")


