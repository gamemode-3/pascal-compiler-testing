program IfElseUseInThen;

var
    a, b: integer;
    c: string;

begin
    a := 4;
    b := 10;
    c := 'c :D';
    // c ist live, auch wenn es nur 
    // von einem branch genutzt wird
    if a < 2 then
        writeln(c)
    else
        writeln('no c :(');
    writeln(b)
end.

// [[LIVENESS_REGISTERS:3]]