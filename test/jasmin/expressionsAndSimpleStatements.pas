program Sample;

var 
  x : double;

function Foo() : integer;
var
  a : integer;
begin
  a := 5;
  Foo := a;
end;

begin
  x := Foo();
  writeln(x);
  writeln(10.0 + x * -4 > 10);
end.