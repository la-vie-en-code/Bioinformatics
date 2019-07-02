#Hamming distance - number of corresponding symbols that differ between two sequences

File = open("SampleHD.txt", "r",)
Seqs = File.read()
#set 2 lists
Seq = Seqs.split("\n")
Seq1 = Seq[0]
Seq2 = Seq[1]
#set the starting count
Count = 0
#loop rules for mismatch
if len(Seq1) == len(Seq2):
    for n in range(len(Seq1)):
        if Seq1[n] != Seq2[n]:
            Count += 1
#result
print(Count)
       