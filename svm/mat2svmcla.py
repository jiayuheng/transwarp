f1=open('traindataL.m','rb')
f2=open('testdataL.m','rb')

def m2svmcla(f):
    for line in f.readlines():
        print line.strip().split('\t')

m2svmcla(f1)
