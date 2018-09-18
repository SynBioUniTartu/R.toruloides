
optfile = open('optimization.txt')

#Codons to be optimized are written here.
#Format is: 'Amino acid letter:codons to be optimized:new codon'
#Please see example file.
#File should be in the same folder as the script


AA = list()
tobeopt = list()
opt = list()

for line in optfile:
    line = line.split(':')
    AA.append(line[0])
    tobeopt.append(line[1].lower())
    opt.append(line[2].strip().lower())
    
codefile = input('Please write the file name here (ex. input.txt): ')
seq = open(codefile)
#Sequence file
#Text file should be in the same folder as the script
#Text file should not contain any spaces, lines, or numbers

bases = list()

for nts in seq:
    for letter in nts:
        bases.append(letter)

codons = list()

for i in range(0,len(bases)):
    if (i+1)%3 == 0:
        codon = bases[i-2] + bases[i-1] + bases[i]
        codons.append(codon.lower())


optimized = list()

for codon in codons:
    for i in range(0,len(tobeopt)):
        if codon in tobeopt[i]:
            codon = opt[i]
    optimized.append(codon)


genoptimized = ''
        
for optcodon in optimized:
    genoptimized = genoptimized + optcodon



outputfile = input('Please write the output file name here (ex. output.txt): ')
 
with open(outputfile, 'w') as text_file:
    text_file.write(genoptimized)

#Optional: you can use 'text_file.write(genoptimized.upper())' to get uppercase nucleotides


    
