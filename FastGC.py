#open fasta file
fasta = open("rosalind_gc-3.txt","r")
#arrange fasta to get ID and seq
IDSEQ = ''.join([x.strip('\r\n') for x in fasta.readlines()]).split('>Rosalind_')
#create a fasta dic
fastdic = {}
del IDSEQ[0]
# total and GC count from seq
for nuc in IDSEQ:
    GC = 0;
    Total=0;
    DNA = str(nuc[4:])
    for n in DNA:
        Total +=1
        if n =='C' or n =='G':
            GC+=1
    fastdic[nuc[:4]]=(100.000*GC)/Total
#order the %GC
TOP = max(fastdic, key=fastdic.get)
print ("Rosalind_"+str(TOP)+'\n'+("{0:.6f}".format(round(fastdic[TOP],6))))