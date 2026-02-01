program ReturnValue;

function Foo () : integer;
var
    a: integer;
begin
    Foo := 0;
    a := 10;
    // hier sind a und Foo live
    writeln(a);
end;

begin
end.

// [[LIVENESS_REGISTERS:2]]