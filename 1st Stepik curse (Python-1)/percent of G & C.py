genome = input()
n = genome.upper().count('G') + genome.upper().count('C')
print(100 * n / len(genome))