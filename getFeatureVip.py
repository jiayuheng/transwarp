def getfeature(diroffile):
    f=open(diroffile,'rb')
    userID={}
    userMoney={}
    userMoneyDetail={}
    MCC={}
    MCCMoney={}
    feature={}
    for line in f.readlines():
    #print line.strip().split(' ')[2]#user id
        if line.strip().split(' ')[2] in userID:
            userID[line.strip().split(' ')[2]]=userID[line.strip().split(' ')[2]]+1
            userMoney[line.strip().split(' ')[2]]=userMoney[line.strip().split(' ')[2]]+int(line.strip().split(' ')[4])
            userMoneyDetail[line.strip().split(' ')[2]].append(int(line.strip().split(' ')[4]))
        if line.strip().split(' ')[2] not in userID:
            userID[line.strip().split(' ')[2]]=1
            userMoney[line.strip().split(' ')[2]]=int(line.strip().split(' ')[4])
            userMoneyDetail[line.strip().split(' ')[2]]=[]
            userMoneyDetail[line.strip().split(' ')[2]].append(int(line.strip().split(' ')[4]))
        if line.strip().split(' ')[3] in MCC:
            MCC[line.strip().split(' ')[3]]=1+MCC[line.strip().split(' ')[3]]
            MCCMoney[line.strip().split(' ')[3]]=MCCMoney[line.strip().split(' ')[3]]+int(line.strip().split(' ')[4])
        if line.strip().split(' ')[3] not in MCC:
            MCC[line.strip().split(' ')[3]]=1
            MCCMoney[line.strip().split(' ')[3]]=int(line.strip().split(' ')[4])

    for key in userID:
        feature[key]=[userID[key],userMoney[key],userMoney[key]/userID[key],max(userMoneyDetail[key])]
    print len(feature)
    #print userMoneyDetail
    return feature
feature1409=getfeature('./1409')
feature1410=getfeature('./1410')
feature1411=getfeature('./1411')
feature1412=getfeature('./1412')
feature1501=getfeature('./1501')

#print feature1409
print "num of id 09",len(feature1409)
print "num of id 10",len(feature1410)
print "num of id 11",len(feature1411)
print "num of id 12",len(feature1412)
print "num of id 1501",len(feature1501)

def getvipfeature(feature):
    vipfeature={}
    for key in feature:
        if feature[key][0]>10 or feature[key][1]>10000:
            vipfeature[key]=feature[key]
    print len(vipfeature),len(feature),float(len(vipfeature))/float(len(feature))
    return vipfeature


vip1409=getvipfeature(feature1409)
vip1410=getvipfeature(feature1410)
vip1411=getvipfeature(feature1411)
vip1412=getvipfeature(feature1412)
vip1501=getvipfeature(feature1501)

#get label
def getlabelcount(feature,traindata):
    vip={}
    for key in traindata:
        if key not in feature:
            vip[key]=0
        if key in feature:
            vip[key]=feature[key][0]
    return vip

def getlabelmoney(feature,traindata):
    vip={}
    for key in traindata:
        if key not in feature:
            vip[key]=0
        if key in feature:
            vip[key]=feature[key][1]
    return vip

def dict2m(inputdict,filename):
    f=open(filename,'wb')
    for key in inputdict:
        f.write(str(key)+'\t')
        for item in inputdict[key]:
            f.write(str(item)+'\t')
        f.write('\n')
    f.close()
        

def gettraindata(dict1,dict2,dict3):
    traindata={}
    for key in dict1:
        traindata[key]=dict1[key]
    for key in dict2:
        if key in traindata:
            for item in dict2[key]:
                traindata[key].append(item)
        if key not in traindata:
            traindata[key]=[]
            for item in dict2[key]:
                traindata[key].append(item)
            for item in dict2[key]:
                traindata[key].append(item)
    for key in traindata:
        if key not in dict2:
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
    for key in dict3:
        if key in traindata:
            for item in dict3[key]:
                traindata[key].append(item)
        if key not in traindata:
            traindata[key]=[]
            for item in dict3[key]:
                traindata[key].append(item)
            for item in dict3[key]:
                traindata[key].append(item)
            for item in dict3[key]:
                traindata[key].append(item)
    for key in traindata:
        if key not in dict3:
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
#    for key in traindata:
#        print len(traindata[key])
#    for key in dict1:
#        print len(dict1[key])
#    for key in dict2:
#        print len(dict2[key])
#    for key in dict3:
#        print len(dict3[key])
    return traindata
traindata= gettraindata(vip1409,vip1410,vip1411)
testdata= gettraindata(vip1410,vip1411,vip1412)
datayuce=gettraindata(vip1411,vip1412,vip1501)
#for key in traindata:  #12
#    print len(traindata[key])
#    print key
#    print traindata[key]

viptraincount=getlabelcount(feature1412,traindata)
viptestcount=getlabelcount(feature1501,testdata)

viptrainmoney=getlabelmoney(feature1412,traindata)
viptestmoney=getlabelmoney(feature1501,testdata)

#for key in traindata:  #12
#    print len(traindata[key])
#    print key
#    print traindata[key]

#print viptrainmoney
print "tarin vip:",len(viptraincount)
print "test vip",len(viptestcount)
#dict2m(traindata,'traindata.m')
#dict2m(liushi,'label.m')
def data2label(traindata,label):
#    for key in traindata:#13#12
#        print len(traindata[key])
#        print label[key]
#        print traindata[key]
    res={}
    for key in traindata:
        res[key]=[]
        for item in traindata[key]:
            res[key].append(item)
        #res[key]=traindata[key]
        res[key].append(label[key])
#        print data[key]
#        print label[key]
#    for key in res:
#        print len(res[key])
    return res
    

#for key in traindata:#12
#    print len(traindata[key])
#    print key
#    print traindata[key]
traindataLcount=data2label(traindata,viptraincount)
traindataLmoney=data2label(traindata,viptrainmoney)
testdataLcount=data2label(testdata,viptestcount)
testdataLmoney=data2label(testdata,viptestmoney)
#for key in traindata:#14#12
#    print len(traindata[key])
#    print key
#    print traindata[key]

dict2m(traindataLcount,'./matlab/traindataLcount.m')
dict2m(testdataLcount,'./matlab/testdataLcount.m')
dict2m(traindataLmoney,'./matlab/traindataLmoney.m')
dict2m(testdataLmoney,'./matlab/testdataLmoney.m')
print traindataLcount
for key in traindataLcount:
    print key
    print traindataLcount[key]



dict2m(datayuce,'./res/q2.m')
