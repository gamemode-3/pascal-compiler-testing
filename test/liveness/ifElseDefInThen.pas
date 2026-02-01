program IfElseDefInThen;

var
    a: integer;
    b: string;

begin
    b := 'sneakyyy';
    a := 4;
    // hier sind a und b live
    if a < 2 then
        b := 'c :D'
    else;
    writeln(b)
end.

// [[LIVENESS_REGISTERS:2]]