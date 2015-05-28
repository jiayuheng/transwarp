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

    #print "num of user"
    #print len(userID)
    #for key in userID:
    #    if userID[key] > 1000:
    #        print key,userID[key]

    #vip_count=0
    #for key in userMoney:
    #    if userMoney[key] > 100000:
    #        print key,userMoney[key]
    #        vip_count+=1

    #print vip_count
    #print len(MCC)
    #print MCCMoney
    for key in userID:
        feature[key]=[userID[key],userMoney[key],userMoney[key]/userID[key],max(userMoneyDetail[key])]
    #    print feature[key]
    #    print userMoneyDetail[key]
    #    print max(userMoneyDetail[key])
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

#get label
def getlabel(feature,traindata):
    liushi={}
    vip={}
    middle={}
    c1={}
    c2={}
    c3={}
    for key in traindata:
        if key not in feature:
            liushi[key]=''
    for key in feature :
        if (feature[key][0]<2 or feature[key][1]<100) and (key in traindata):
            liushi[key]=''
        if (feature[key][0]>=10 or feature[key][1]>=10000) and key in traindata:
            vip[key]=''
        #if feature[key][0]>=2 and feature[key][0]<10 and feature[key][1]>=100 and feature[key][1]<10000:
        #    middle[key]=''
        #if feature[key][0]<2 and feature[key][1]>=100 and feature[key][1]<10000:
        #    middle[key]=''
        #if feature[key][1]<100 and feature[key][0]>=2 and feature[key][0]<10:
        #    middle[key]=''
        #if feature[key][0]<=2:
        #    c1[key]=''
        #if feature[key][0]>2 and feature[key][0]<10:
        #    c2[key]=''
        #if feature[key][0]>=10:
        #    c3[key]=''
        #if feature[key][1]<=100:
        #    c1[key]=''
        #if feature[key][1]>100 and feature[key][1]<10000:
        #    c2[key]=''
        #if feature[key][1]>=10000:
        #    c3[key]=''
    #print len(c1),len(c2),len(c3),len(c1)+len(c2)+len(c3)
    #print len(liushi),len(vip),len(middle),len(liushi)+len(vip)+len(middle)
    print len(liushi),len(vip),len(liushi)+len(vip)
    return liushi

def dict2m(inputdict,filename):
    f=open(filename,'wb')
    for key in inputdict:
        f.write(str(key)+'\t')
        for item in inputdict[key]:
            f.write(str(item)+'\t')
        f.write('\n')
    f.close()
        

#getlabel(feature1412)
#print len(feature1412)

#getlabel(feature1501)
#print len(feature1501)

#dict2m(feature1412,'1412.m')
#dict2m(feature1411,'1411.m')
#dict2m(feature1410,'1410.m')
#dict2m(feature1409,'1409.m')
#dict2m(feature1501,'1501.m')

def gettraindata(dict1,dict2,dict3):
    traindata={}
    for key in dict1:
        traindata[key]=dict1[key]
    for key in dict2:
        if key in traindata:
            for item in dict2[key]:
                traindata[key].append(item)
        if key not in traindata:
            traindata[key]=[0,0,0,0]
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
            traindata[key]=[0,0,0,0,0,0,0,0]
            for item in dict3[key]:
                traindata[key].append(item)
    for key in traindata:
        if key not in dict3:
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
            traindata[key].append(0)
    return traindata
traindata= gettraindata(feature1409,feature1410,feature1411)
testdata= gettraindata(feature1410,feature1411,feature1412)
res=traindata
#for key in res:
#    print res[key]
print len(res)        

liushitrain=getlabel(feature1412,traindata)
liushitest=getlabel(feature1501,testdata)

print "tarin liushi:",len(liushitrain)
print "test liushi",len(liushitest)
#dict2m(traindata,'traindata.m')
#dict2m(liushi,'label.m')
for key in traindata:
    if key in liushitrain:
        traindata[key].append(0)
    if key not in liushitrain:
        traindata[key].append(1)
for key in testdata:
    if key in liushitest:
        testdata[key].append(0)
    if key not in liushitest:
        testdata[key].append(1)
dict2m(traindata,'traindataL.m')
dict2m(testdata,'testdataL.m')

####out put
datayuce=gettraindata(feature1411,feature1412,feature1501)
dict2m(datayuce,'./res/q1.m')

