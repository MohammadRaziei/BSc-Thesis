function json = fcn(Vehicle_1,Vehicle_1_Sensors_1,Collision_valid,Collision_1,Collision_2,done)
 %BY @MohammadRaziei
coder.extrinsic('num2str','bdroot','get_param');
% % % % % % % % % % % % % % % % % % % % % % % % % 
%Settings :
    Object = '0';
%Setup Precisions
    pInput = 5;
    pt = 10;
%Number Of Vehicles
    N_vehicles = 1;
%Names
    vehicle_name = 'Toyota_Yaris_Hatchback_1';
% --------------------more--------------------
Core_Len = 85;
Veh_Len = 101;
NColl = 4;
Ninput = N_vehicles * 7 + NColl;
% ----------------more-than-more--------------
input = [Vehicle_1(:)];
input(isnan(input)) = 0;
% % % % % % % % % % % % % % % % % % % % % % % % %
p = pInput + 7;

LCore = Core_Len*10;
LVeh = Veh_Len*10;
LSens = length(Vehicle_1_Sensors_1);


u = num2str([input(:);-1], ['% .' num2str(pInput) 'e ']);
sss = 1:p;


t = num2str(round(get_param(bdroot,'SimulationTime'),pt),['%0.' num2str(pt) 'f ']);
ts = (32*ones(1,pt));
ts(1:pt) = t(1,1:pt);

colli = num2str(int8([Collision_1;Collision_2;99]),'% 2.f');
col1 = colli(1,1:2);
col2 = colli(2,1:2);


len = 301+pt+LSens;
json = uint8(32*ones(1,len));

json2 = ['{"Time":' ts ',"Object":' Object ',"Vehicles":[{"name":"' vehicle_name ...
    '","data":{"Position":{"x":' u(1,sss) ',"y":' u(2,sss) ',"z":' u(3,sss) ...
    '},"Rotation":{"x":' u(4,sss) ',"y":' u(5,sss) ',"z":' u(6,sss) '},"Velocity":' u(7,sss) ...
    '},"Sensors":[' Vehicle_1_Sensors_1 ']}],"Collision":{"Occurred":' num2str(int8(Collision_valid),'%1.f')...
    ',"col_1":' col1 ',"cal_2":' col2 '},"done":' num2str(done,'%1.f') '}'];
json(1:len)= json2;
json = uint8(json);
