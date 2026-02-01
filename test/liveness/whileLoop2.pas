program WhileLoop2;

var
    a, b, c: integer;

begin
    a := 4;
    b := 10;
    while a >= 2 do
    begin
        a := b;
        c := 1;     // | a muss hier live sein!
        b := b - c; // | es wird in der condition benutzt!
    end;
end.

// [[LIVENESS_REGISTERS:3]]