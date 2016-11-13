# Created by Ibukun on 7/30/2016.
'''

    This program reads two nucleotide sequences, converts them to proteins and compares them.
    One of the nucleotide sequences is a mutant of the other, so the expected result is a confirmation
    of this and the location of the mutations.
    
'''


# opening the Fasta format files
infile1 = open("hbb.txt")  # human hemoglobin subunit gen
infile2 = open("hbb_mutant.txt") # mutant of hemoglobin gene tha causes sicklecell anemia

# read the nucleotide sequence for human hemoglobin subunit
infile1.readline()  # to discard first line in FASTA format file
hbb_seq = infile1.read()
hbb_seq = hbb_seq.replace('\n', '')  # remove newline character
len_hbb_seq = len(hbb_seq)
print "length human hemoglobin sequence is:", len_hbb_seq

# read the mutant sequence
infile2.readline()  # to discard first line in FASTA format file
mutant = infile2.read()
mutant = mutant.replace('\n', '')
len_mutant = len(mutant)
print "length of MUTANT human hemoglobin sequence is:", len_mutant
# ---------------------------------------------------------


# set up amino acid dictionary for dna translation.
# SEE: Codon_to_amino Acid table for reference
letters = ('G', 'A', 'C', 'T')
codons = []  # a sequence of three nucleotides that together form a unit of genetic code in a DNA or RNA molecule.
for a in letters:
    for b in letters:
        for c in letters:
            codons.append(a + b + c)  # this creates a list of all possible codons (permutations of DNA)
print codons
print 'length of all possible DNA codes: ', len(codons)  # 64 is expected
#   A string of all amino acids represented by the first letter of their names
amino_acid = 'ggggeeddaaaavvvvrrsskknnttttmiiirrrrqqhhppppllllwxccxxyyssssllff'
amino_acid = amino_acid.upper()
amino_acid_dictionary = {}
# now create a dictionary of amino acid DNA pairs. e.g {'GGG': 'G','AUG': 'M','UUU': 'P'}
for i in range(64):
    amino_acid_dictionary[codons[i]] = amino_acid[i]
print '================================================================================='
# test the dictionary to see that it maps correctly.
print "This expected {'GGG': 'G','ATG': 'M','TTT': 'F'}"
print "GGG:", amino_acid_dictionary["GGG"]
print "ATG:", amino_acid_dictionary["ATG"]
print "TTT:", amino_acid_dictionary["TTT"]

# now lets make the protein (amino acid sequence) from the human hemoglobin dna sequence
protein = ''
for i in range(0, len_hbb_seq, 3):  # codons are in triplets
    codon = hbb_seq[i:i+3]
    aminoacid = amino_acid_dictionary[codon]  # using dictionary to create amino acid equivalent
    protein += aminoacid  # concatenating the amino acids to form a protein
# the same for the mutant sequence
mutant_protein = ''
for i in range(0, len_mutant, 3):
    codon = mutant[i:i+3]
    aminoacid = amino_acid_dictionary[codon]
    mutant_protein += aminoacid

print '================================================================================='
# check if the two proteins are the same. they shouldnt be
if protein == mutant_protein:
    print 'The Sequences are the same.'
else:
    print 'The Sequences are different.'
    # since they are different, locate and display the locations of mutation
    for i in range(len(protein)):
        if protein[i] != mutant_protein[i]:
                print "Amino acid", protein[i], "at location", str(i), "changed to", mutant_protein[i]
print '================================================================================='