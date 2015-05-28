f=open('dataByDay','rb')
userID={}
userMoney={}
MCC={}
MCCMoney={}
for line in f.readlines():
    #print line.strip().split(' ')[2]#user id
    if line.strip().split(' ')[2] in userID:
        userID[line.strip().split(' ')[2]]=userID[line.strip().split(' ')[2]]+1
        userMoney[line.strip().split(' ')[2]]=userMoney[line.strip().split(' ')[2]]+int(line.strip().split(' ')[4])
    if line.strip().split(' ')[2] not in userID:
        userID[line.strip().split(' ')[2]]=1
        userMoney[line.strip().split(' ')[2]]=int(line.strip().split(' ')[4])
    if line.strip().split(' ')[3] in MCC:
        MCC[line.strip().split(' ')[3]]=1+MCC[line.strip().split(' ')[3]]
        MCCMoney[line.strip().split(' ')[3]]=MCCMoney[line.strip().split(' ')[3]]+int(line.strip().split(' ')[4])
    if line.strip().split(' ')[3] not in MCC:
        MCC[line.strip().split(' ')[3]]=1
        MCCMoney[line.strip().split(' ')[3]]=int(line.strip().split(' ')[4])

print "num of user"
print len(userID)
print "average jilu of id"
print 1393020/len(userID)
#for key in userID:
#    if userID[key] > 1000:
#        print key,userID[key]

vip_count=0
for key in userMoney:
    if userMoney[key] > 100000:
#        print key,userMoney[key]
        vip_count+=1

#print vip_count

print "num of MCC"
print len(MCC)
#print MCCMoney

