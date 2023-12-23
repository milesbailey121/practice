with open(r"ROSALIND\Bioinformatics_Stronghold\[3]ComplementingaStrandofDNA\rosalind_revc.txt") as file:
    nucleotides = file.read()
    
revc = []
for nucleotide in nucleotides:
    match nucleotide:
        case "A":
            revc.append("T")
        case "T":
            revc.append("A")
        case "G":
            revc.append("C")
        case "C":
            revc.append("G")

print("".join(revc[::-1]))