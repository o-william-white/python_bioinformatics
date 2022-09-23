
# at content
def at_content(seq):
    return (seq.count("A") + seq.count("T")) / len(seq)
assert at_content("ATCG") == 0.5

# gc content
def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq)
assert at_content("ATCG") == 0.5

# sequence complexity
# percentage of bases that are different from their next base
def sequence_complexity(seq):
    previous_base, differences = None, 0
    for base in seq:
        if previous_base == None:
            previous_base = base
        else:
            if base != previous_base:
                differences += 1
                previous_base = base
    complexity = differences / (len(seq)-1)
    return complexity
assert sequence_complexity("ATCGA") == 1.0
assert sequence_complexity("AACAA") == 0.5

