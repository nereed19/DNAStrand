# Given a base, gives the complement base
DNA_complement = { 
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

print DNA_complement['A'] #returns C
print DNA_complement['T'] #returns A
print DNA_complement['C'] #returns G
print DNA_complement['G'] #returns C

# Given a string of bases, returns a string of complementary bases
def create_complement(s1): 
    s2 = ""
    for base in s1:
        s2 += DNA_complement[base]
    return s2

print create_complement("G") #returns C
print create_complement("ATCG") #returns TAGC
print create_complement("ATCAGTTAGCATGACG") #returns TAGTCAATCGTACTGC

# Given two strings of bases, returns a boolean indicating whether they are a valid pairing
def check_strand(s1, s2):
    slen = len(s1)
    for i in range(slen):
        if s1[i] == "A":
            if s2[i] != "T":
                return False
        elif s1[i] == "T":
            if s2[i] != "A":
                return False
        elif s1[i] == "C":
            if s2[i] != "G":
                return False
        elif s1[i] == "G":
            if s2[i] != "C":
                return False
    return True

def check_strand2(s1, s2): # An even better way to check if two strands are valid
    return create_complement(s1) == s2

print check_strand("A","T") #true
print check_strand("ATC","TAG") #true
print check_strand("ATC","AAG") #false

print check_strand2("A","T") #true
print check_strand2("ATC","TAG") #true
print check_strand2("ATC","AAG") #false
