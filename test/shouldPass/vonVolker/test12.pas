program test12;

var
    z : integer;

function hi(a , b : integer; c, d : string; g : boolean): integer;
var
    i : integer;
begin
    i := b +5;
    hi := 1;
end;

begin
    z := hi(1+7,z, 'true','ho', true or false);
end.