f=open('event.csv','rb')
fw=open('data','wb')
for line in f.readlines():
    #print line.strip().split(',')
    dataperline=''
    dataperlinelist=line.strip().split(',')
    for item in dataperlinelist:
        dataperline=dataperline+item+'\t'
    fw.write(dataperline+'\n')

f.close()
fw.close()
    
