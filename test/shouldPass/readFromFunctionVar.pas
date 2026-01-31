program Sample;

function foo() : integer;
begin
    foo := 42;
    if foo > 0 then
        foo := foo + 1;
end;

begin
    writeln(foo());
end.