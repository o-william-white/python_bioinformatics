
import sys
import os
from ete3 import Tree

# run as
# root_multiple_trees.py input_file file_ending output_file outgroup1,outgroup2,etc

# input agruments
input_file  = sys.argv[1]
file_ending = sys.argv[2]
output_file = sys.argv[3]
outgroups   = sys.argv[4]

# mk output dir if not already present
if not os.path.exists(output_file):
    os.mkdir(output_file)

# split outgroups
outgroups = outgroups.split(",")

# root function
def root_tree(tree, outgroups): 
    # if single outgroup providied, find node
    if len(outgroups) == 1:
        node = tree&outgroups[0]
        print("Setting root")
        tree.set_outgroup(node)
    else:
        # else, find ancestor
        ancestor = tree.get_common_ancestor(outgroups)
        # check if ancestor is already the current root
        # else, root on ancestor
        if tree == ancestor:
            print("MRCA of outgroups is the current root node")
        else:
            print("Setting root")
            tree.set_outgroup(ancestor)

# for loop through files in dir
for file in os.listdir(input_file):
    if file.endswith(file_ending):
        # file basename
        basename = file.replace(file_ending, "")
        # read tree
        print("Reading file: " + basename)
        tree = Tree(open(input_file + "/" + file, "r").read().rstrip("\n"))
        # run function to root tree
        root_tree(tree, outgroups)

        # write outfile
        print("Writing output")
        outfile = open(output_file + "/" + basename + "_rooted" + file_ending, "w")
        outfile.write(tree.write())
        outfile.close()
        print()


