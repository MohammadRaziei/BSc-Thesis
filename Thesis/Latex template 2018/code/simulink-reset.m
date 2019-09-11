function [done,reset] = fcn(coll,vehicle_info,Auto_reset,cmd)
done=false;
if (vehicle_info(1) >= 750)
    done = true;
end

done = or(done,coll);
reset = not(or(and(done,Auto_reset),cmd));
end