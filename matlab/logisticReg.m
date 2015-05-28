
%% Initialization
clear ; close all; clc

%% Load Data


%data = load('ex2data2.txt');
load /home/jiayuheng/mianshi/transwarp/traindataL.m
load /home/jiayuheng/mianshi/transwarp/testdataL.m
X = traindataL(:, 2: 13); y = traindataL(:, 14);

X(:,1)=(X(:,1)-12.5)/2391;
X(:,5)=(X(:,5)-12.5)/2391;
X(:,9)=(X(:,9)-12.5)/2391;
X(:,2)=(X(:,2)-153180)/22646670;
X(:,6)=(X(:,6)-153180)/22646670;
X(:,10)=(X(:,10)-153180)/22646670;
X(:,3)=(X(:,3)-12294)/970465;
X(:,7)=(X(:,7)-12294)/970465;
X(:,11)=(X(:,11)-12294)/970465;
X(:,4)=(X(:,4)-153180)/22646670;
X(:,8)=(X(:,8)-153180)/22646670;
X(:,12)=(X(:,12)-153180)/22646670;

%% pca
[pc,score,latent,tsquare] = princomp(X);

pcaMatrix=pc(:,1:5);

%X=X*pc(:,1:2);




%% train  model
%X = mapFeature(X(:,1), X(:,2));
initial_theta = zeros(size(X, 2), 1);


lambda =19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ;

% Set Options
options = optimset('GradObj', 'on', 'MaxIter', 800);

% Optimize
[theta, J, exit_flag] = ...
	fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);


p = predict(theta, X,0.5);

fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);

%% test data
X = testdataL(:, 2: 13); y = testdataL(:, 14);

X(:,1)=(X(:,1)-12.5)/2391;
X(:,5)=(X(:,5)-12.5)/2391;
X(:,9)=(X(:,9)-12.5)/2391;
X(:,2)=(X(:,2)-153180)/22646670;
X(:,6)=(X(:,6)-153180)/22646670;
X(:,10)=(X(:,10)-153180)/22646670;
X(:,3)=(X(:,3)-12294)/970465;
X(:,7)=(X(:,7)-12294)/970465;
X(:,11)=(X(:,11)-12294)/970465;
X(:,4)=(X(:,4)-153180)/22646670;
X(:,8)=(X(:,8)-153180)/22646670;
X(:,12)=(X(:,12)-153180)/22646670;



%X=X*pc(:,1:5);
%X = mapFeature(X(:,1), X(:,2));
p = predict(theta, X,0.5);

fprintf('Test Accuracy: %f\n', mean(double(p == y)) * 100);

%% resout
load /home/jiayuheng/mianshi/transwarp/res/q1.m
X = q1(:, 2: 13); id = q1(:, 1);

X(:,1)=(X(:,1)-12.5)/2391;
X(:,5)=(X(:,5)-12.5)/2391;
X(:,9)=(X(:,9)-12.5)/2391;
X(:,2)=(X(:,2)-153180)/22646670;
X(:,6)=(X(:,6)-153180)/22646670;
X(:,10)=(X(:,10)-153180)/22646670;
X(:,3)=(X(:,3)-12294)/970465;
X(:,7)=(X(:,7)-12294)/970465;
X(:,11)=(X(:,11)-12294)/970465;
X(:,4)=(X(:,4)-153180)/22646670;
X(:,8)=(X(:,8)-153180)/22646670;
X(:,12)=(X(:,12)-153180)/22646670;

res = predict(theta, X,0.5);


