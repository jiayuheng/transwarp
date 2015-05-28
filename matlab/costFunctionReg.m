function [J, grad] = costFunctionReg(theta, X, y, lambda)

m = length(y); % num of training examples
J = 0;
grad = zeros(size(theta));

%%  cost function
for i=1:m
    J=J+(-1*y(i)*log(sigmoid(X(i,:)*theta))-(1-y(i))*log(1-sigmoid(X(i,:)*theta)))/m;
end
for i=2:max(size(theta))
    J=J+(theta(i)*theta(i)*lambda)/(2*m);
end

%% gradient 
    grad_updata=0;
for i=1:m
    grad_updata=grad_updata+(sigmoid(X(i,:)*theta)-y(i))*X(i,1);
end
    grad(1)=(grad_updata)/m;
    grad_updata=0;
for j=2:max(size(theta))
    for i=1:m
        grad_updata=grad_updata+(sigmoid(X(i,:)*theta)-y(i))*X(i,j);
    end
    grad(j)=(grad_updata+lambda*theta(j))/m;
    grad_updata=0;
end


end
