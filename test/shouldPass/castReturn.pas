program Sample;

function foo() : double;
var
    x : integer = 3;
begin
    foo := x;
end;

begin
  writeln(foo());
end.