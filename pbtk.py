import argparse

# create main parser
parser = argparse.ArgumentParser(
        prog='pbtk.py',
        description='python bioinformatic tool kit',
        epilog='Thank you for using pbtk!')

# create subparsers for different subcommands
subparsers = parser.add_subparsers(dest='subcommand', title='Input type', description='', metavar = '')

# subparser fasta
subparser_fasta = subparsers.add_parser('fasta',         help='Individual fasta')
subparser_fasta.add_argument('--input',                  help='Input fasta', required = True)
subparser_fasta_options = subparser_fasta.add_mutually_exclusive_group(required=True)
subparser_fasta_options.add_argument('--length',         help='Sequence lengths')
subparser_fasta_options.add_argument('--gc',             help='Sequence GC content')
subparser_fasta_options.add_argument('--at',             help='Sequence GC content')

# subparser fastq
subparser_fastq = subparsers.add_parser('fastq', help='Unpaired or paired for fastq')
subparser_fastq.add_argument('--input',     help='Input fastq forawrd or unpaired', required = True)
subparser_fastq.add_argument('--input2',    help='Input fastq reverse',             required = False)
subparser_fastq_options = subparser_fastq.add_mutually_exclusive_group(required=True)
subparser_fastq_options.add_argument('--n_reads',   help='Number of reads')
subparser_fastq_options.add_argument('--length',    help='Sequence_lengths')

# subparser sam/bam
subparser_sam = subparsers.add_parser('sam',  help='SAM or BAM')
subparser_sam.add_argument('--input',         help='Input SAM or BAM', required = True)
subparser_sam_options = subparser_sam.add_mutually_exclusive_group(required=True)
subparser_sam_options.add_argument('--plot_coverage', help='Plot coverage')

# Parse the command-line arguments
args = parser.parse_args()


if args.subcommand == 'fasta':
    print(f'Fasta subcommand selected')
    # Add your code for subcommand1 here

elif args.subcommand == 'fastq':
    print(f'Fastq subcommand selected')
    # Add your code for subcommand2 here

else:
    print('No input type selected. Use -h or --help for usage information.')
