BASES = ['A','C','G','T']

def count_base(s, base):
    count = 0
    for c in s:
        if c == base:
            count = count + 1
        
    return count

def count_bases(s):
    counts = []
    for base in BASES:
        counts.append(count_base(s, base))
    return counts

counts = count_bases('CCACCTACGTGCCAGGCTATTACCGACCCAGCAGGCCGCATAACGGACTGGGTGGCCGTCCAGACGGTGCCTAGTCACGCGCGTATTGGCCAGTTTGGAGGACGTGTAGCCTTTGCTGATAAGAAATTAACGTTCCATACACCCCAGATCTGATTCTGAGAATCCGGACTCGCGGGTTGCTGTTTATTGAATTCGTAGTATGATAACGTGCAGTAGCTACGCGAGCTACACGAGACTTAGATATTTTAGCCGCTGCCTCCGGGCGAGATGTGTAATCAGTGCGGGTAACGTTAAGAATCGTGGCCTTGGGGGCAACCTCTTGCATTCTCGTCTGATGTTGGATTGTCGACTGAAAAGATGCCTAGGGGGTGTTCACTGCAATAAAGGATGCCTGAATGTGCAATTGGTATCAGGCTCAAACTCCATAGACGTTTGTTATTCATTGACCCCCAGACCAGAAACCTCGGTATAACATGGTAATCACACGATTAGTATCACGTGCCACAAACTCTAATGAAGACGTGTTAACCTCTCGTCAGGTCGATGGGGACCAGTTCATGAGGTCTTGCGGCGCCGGTCGTGGCTGGATACACGCTATACACTGCAGCGGTAGAAGAGTGGCCCATACTCGGATCTTTAGCACTATGAAGGCCCCATCAACGTCGAAAAAGGCTACTTACACAATACCTAACAGTTCTAACCACGGAGTGTTTTCGTTTGCTAATGAGGACAGCCGATTGGCTTTGACCCCCGAGGATCACGAATTCTGGCTTTCGGCGCATAGCCGCCTTCGATGACTGCGCGTGTCTACGATCGAACCCACCTTGATGTTGACGCACCTTAGTTGCAACGACAAGACCCGTAAAATATTCCGATTCTGACTTGAAGTTAATCTATAATAGGTTACGGAGTAAATTTCCCTAATGTACTCATCAGTATCTGTGCTCATGTCAGCGACTTT')
for c in counts:
    print(c, end=' ')

print()