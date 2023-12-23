with open(r"ROSALIND\Bioinformatics_Stronghold\[4]RabbitsandReccurenceRelations\rosalind_fib.txt") as file:
    input = file.read()

# A key observation is that the number of offspring in any month is equal to the numbe rof rabbits that were alive two months ago
# As a results, If Fn representas the rabbit pairs alive after the n-th month, we obtain the sequence having terms Fn that are dfeined by the recurrent rleation 

n = int(input[0:2])
k = int(input[3:4])

n = 5
k = 3
F = [None] * (n+3)
F[0] = 1 
F[1] = 1



for i in range(2, (n+3)):
    F[i] = F[i - 1] + F[i - 2]
    F[i] += F[i]
    


for items in F:
    print(items)