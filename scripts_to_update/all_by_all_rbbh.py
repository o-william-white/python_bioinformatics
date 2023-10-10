
import sys
import pandas as pd
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline

# get input fasta
input_fasta = sys.argv[1]
nthreads = sys.argv[2]

# makeblastdb
makeblastdb_cline = NcbimakeblastdbCommandline(dbtype="nucl", input_file=input_fasta)
print('Creating blast database')
print('Cmd: "' + str(makeblastdb_cline) + '"')
stdout, stderr = makeblastdb_cline()

# blastn
blastn_cline = NcbiblastnCommandline(task='blastn', query=input_fasta, db=input_fasta, out='blast_out.txt', outfmt=6, evalue='1e-20', num_threads=nthreads)
print('Running blastn search')
print('Cmd: "' + str(blastn_cline) + '"')
stdout, stderr = blastn_cline()

# read blast tabular output
print('Reading blast hits')
blast = pd.read_table('blast_out.txt', sep='\t', header=None)

# set headers of blast output
headers = ['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
blast.columns = headers

# remove rows where the query hits itself
blast = blast[blast.qseqid != blast.sseqid]

# sort blast output by qseqid and bitscore
print('Filtering for best hits')
blast = blast.sort_values(by=['qseqid', 'bitscore'], ascending=[True, False])

# take the first blast hit per qseqid
blast = blast.drop_duplicates('qseqid')

# merge blast with itself
# join sseqid left to qseqid right
print('Identifying reciprocal best blast hits')
rbbh = pd.merge(blast, blast[['qseqid','sseqid','evalue']], left_on='sseqid', right_on='qseqid', how='outer')

# remove rows with rbbh
rbbh = rbbh[rbbh.qseqid_x == rbbh.sseqid_y]

# function to return sorted comma spearated string of qseqid and sseqid 
def sort_qseqid_sseqid(x):
    # get qseqid_x and sseqid_x 
    x = [x[0], x[1]]
    # sort
    x.sort()
    # join as comma separated
    x=','.join(x)
    return(x)

# add column with sorted comma spearated string of qseqid and sseqid
rbbh['qseqid_sseqid_sorted'] = rbbh.apply(axis=1, func=sort_qseqid_sseqid)

# sort based on comma separated list 
rbbh = rbbh.sort_values(by=['qseqid_sseqid_sorted'])

# write outputs
print('Writing outputs')
blast.to_csv('blast_out_top_hit.txt', sep='\t', index=False)
rbbh.to_csv('blast_out_rbbh.txt', sep='\t', index=False)
