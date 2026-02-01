program IfElseUseInBoth;

var
    a, b: integer;
    c: string;

begin
    a := 4;
    b := 10;
    c := 'c :D';
    // a, b und c sind hier live
    if a < 2 then
        writeln(c)
    else
        writeln(c);
    writeln(b)
end.

// [[LIVENESS_REGISTERS:3]]