program WhileLoop1;

var
    a, b, c: integer;

begin
    a := 4;
    b := 10;
    while a >= 2 do
    begin
        c := 1;     // | a muss hier nicht live sein!
        b := b - c; // |
        a := b;
    end;
end.

// [[LIVENESS_REGISTERS:2]]