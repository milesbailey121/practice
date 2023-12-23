with open(r"ROSALIND\Bioinformatics_Stronghold\[1]CountingDNANucleotide\rosalind_dna.txt") as file:
    oligonucleotide = file.read()

A = 0
T = 0
G = 0 
C = 0
for base in oligonucleotide:
    match base:
        case "A":
            A += 1
        case "T":
            T += 1
        case "G":
            G += 1
        case "C":
            C += 1
            
print(A, C, G, T)

