function p = predict(theta, X,val)


m = size(X, 1); % num of training examples


p = zeros(m, 1);


for i=1:m
    if sigmoid(X(i,:)*theta)<val
        p(i)=0;
    else
        p(i)=1;
    end
end


end
