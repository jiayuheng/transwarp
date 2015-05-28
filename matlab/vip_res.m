clear
clc
load /home/jiayuheng/mianshi/transwarp/matlab/testdataLcount.m
load /home/jiayuheng/mianshi/transwarp/matlab/testdataLmoney.m
load /home/jiayuheng/mianshi/transwarp/matlab/traindataLcount.m
load /home/jiayuheng/mianshi/transwarp/matlab/traindataLmoney.m

load /home/jiayuheng/mianshi/transwarp/res/q2.m 

%% count
rato=max(traindataLcount(:,14));
 traindataLcount(:,14)= traindataLcount(:,14)/rato;
 
testdataLcount(:,14)= testdataLcount(:,14)/rato;

for i=2:13
     max_temp=max(traindataLcount(:,i));
     traindataLcount(:,i)=traindataLcount(:,i)/max_temp;
     testdataLcount(:,i)= testdataLcount(:,i)/max_temp;
     q2(:,i)=q2(:,i)/max_temp;
 end
TrainingData_File=zeros(size(traindataLcount,1),13);
TrainingData_File(:,1)=traindataLcount(:,14);
TrainingData_File(:,2:13)=traindataLcount(:,2:13);

TestingData_File=zeros(size(testdataLcount,1),13);
TestingData_File(:,1)=testdataLcount(:,14);
TestingData_File(:,2:13)=testdataLcount(:,2:13);
  [TrainingTime, TestingTime, TrainingAccuracy, TestingAccuracy,res]=ELM(TrainingData_File, TestingData_File, 0, 200, 'sigmoid',30,q2);
  q2_res_count=res'*rato;
q2_count=[q2(:,1),q2_res_count];

%% money
clear
load /home/jiayuheng/mianshi/transwarp/matlab/testdataLcount.m
load /home/jiayuheng/mianshi/transwarp/matlab/testdataLmoney.m
load /home/jiayuheng/mianshi/transwarp/matlab/traindataLcount.m
load /home/jiayuheng/mianshi/transwarp/matlab/traindataLmoney.m

load /home/jiayuheng/mianshi/transwarp/res/q2.m 

rato=max(traindataLcount(:,14));
 traindataLmoney(:,14)= traindataLmoney(:,14)/max(traindataLmoney(:,14));
 testdataLmoney(:,14)= testdataLmoney(:,14)/max(testdataLmoney(:,14));

 for i=2:13
     max_temp=max(traindataLmoney(:,i));
     traindataLcount(:,i)=traindataLmoney(:,i)/max_temp;
     testdataLcount(:,i)= testdataLmoney(:,i)/max_temp;
     q2(:,i)=q2(:,i)/max_temp;
 end
 
 TrainingData_File=zeros(size(traindataLcount,1),13);
TrainingData_File(:,1)=traindataLcount(:,14);
TrainingData_File(:,2:13)=traindataLcount(:,2:13);
TestingData_File=zeros(size(testdataLcount,1),13);
TestingData_File(:,1)=testdataLcount(:,14);
TestingData_File(:,2:13)=testdataLcount(:,2:13);


   [TrainingTime, TestingTime, TrainingAccuracy, TestingAccuracy,res]=ELM(TrainingData_File, TestingData_File, 0, 200, 'sigmoid',0.01,q2);
  q2_res_money=res'*rato;
q2_money=[q2(:,1),q2_res_money];
 
 