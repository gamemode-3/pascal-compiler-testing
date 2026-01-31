program Sample;

procedure foo();
var
    x : integer;
begin
    x := foo;
    writeln(x);
end;

begin
    foo();
end.