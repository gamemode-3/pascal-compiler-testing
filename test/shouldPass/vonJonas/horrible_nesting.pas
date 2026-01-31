// Just some annoying nesting with and without begin-end blocks of ifs and loops
program HorribleNesting;
var
    n : integer;
begin
    n := 10;
    if (1 > 0) then
    begin
        if (1 > 0) then
        begin
            while (n > 0) do n := (((((((n - 1)))))));
        end else n := 100;
    end;
    
    if (n <> 42) then n:= 42;
end.