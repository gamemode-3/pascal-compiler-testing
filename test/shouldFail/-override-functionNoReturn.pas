program Sample;

function foo(a : integer): integer;
begin
    if a > 10 then
        foo := a;
end;

begin
    writeln(foo(15));
    writeln(foo(0));
end.