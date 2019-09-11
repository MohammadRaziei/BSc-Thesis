function [json,len] = sensor(Range,theta,ID,Velocity)
%BY @MohammadRaziei
Precision = 5;
name = 'AIR_1';
% % % % % % % % % % % % % % % % % % % % % % % % % % % 
coder.extrinsic('num2str','string','strjoin');

n = length(Range);
p = Precision + 7;
len = 56+4*(n+1)+p*n*4+length(name);

ArrSize = p*10+11;
sss = 1:ArrSize;
% Range :
Range_str = string(num2str([Range(:);-1],['% .' num2str(Precision) 'e ']));
Range_str = ['[' char(strjoin(Range_str(1:n) ,',')) ']'];
Range_ = zeros(1,ArrSize);Range_(sss) = Range_str(sss) ;
% theta :
theta_str = string(num2str([theta(:);-1],['% .' num2str(Precision) 'e ']));
theta_str = ['[' char(strjoin(theta_str(1:n) ,',')) ']'];
theta_ = zeros(1,ArrSize);theta_(sss) = theta_str(sss) ;
% ID :
ID_str = string(num2str([ID(:);-1],['% .' num2str(Precision) 'e ']));
ID_str = ['[' char(strjoin(ID_str(1:n) ,',')) ']'];
ID_ = zeros(1,ArrSize);ID_(sss) = ID_str(sss) ;
% Velocity :
Velocity_str = string(num2str([Velocity(:);-1],['% .' num2str(Precision) 'e ']));
Velocity_str = ['[' char(strjoin(Velocity_str(1:n) ,',')) ']'];
Velocity_ = zeros(1,ArrSize);Velocity_(sss) = Velocity_str(sss) ;

json = uint8(32*ones(1,len));
json2 = ['{"name":"' name '","data":{"Range":' Range_ ',"theta":' theta_ ',"ID":' ID_ ',"Velocity":' Velocity_ '}}'];
    
json(1:len)= json2;
json = uint8(json);