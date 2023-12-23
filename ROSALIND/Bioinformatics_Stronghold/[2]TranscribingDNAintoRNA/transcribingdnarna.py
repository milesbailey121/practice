with open(r"C:\Users\miles\GitHub\practice\ROSALIND\Bioinformatics_Stronghold\[2]TranscribingDNAintoRNA\rosalind_rna.txt") as file:
    DNA = file.read()

RNA = []
for nucleotide in DNA:
    if nucleotide == "T":
        RNA.append("U")
    else:
        RNA.append(nucleotide)

print(''.join(RNA))