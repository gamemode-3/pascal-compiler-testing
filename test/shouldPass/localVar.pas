program Sample;

function foo(x : integer) : integer;
var
  y : integer = 4;
begin
  foo := x - y;
end;

begin
  writeln(foo(1));
end.
