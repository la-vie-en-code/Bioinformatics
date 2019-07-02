#Calculate the probability for obtaining a dominant phenotype from a population
##Data
### k = Homo Dom ; m = Hetero Dom/rec and n = Homo rec

def Dominant(k,m,n):
    #prob to have a dominant = 1-prob to have a recive
    t = k+m+n
    #prob for homR - homR
    #chance to have a rec allele in HomR = 100% = 1
    pr1 = (n/t)*(1) * ((n-1)/(t-1))*(1)
    #chance to have Het-homR
    #chance to have a rec allele in Het = 50% = 0,5
    pr2 = (m/t)*(1/2) * (n/(t-1))*(1)
    #chance to have homR - Rec
    pr3 = (n/t)*(1) * (m/(t-1))*(1/2)
    #chance to have het - het
    pr4 = (m/t)*(1/2) * ((m-1)/(t-1))*(1/2)
    #total prob to have a rec phenotype
    prt = pr1 + pr2 + pr3 + pr4
    #prob for a dom phenotype
    prd = 1 - prt
    return prd