program Sample;

function foo(x : integer) : integer;
begin
  foo := x - 1;
end;

function bar(x : integer) : integer;
var
  a : integer = foo(3);
//              ^^^^^^
// Function calls can not be used in variable declarations
begin
  bar := x + a;
end;

begin
  writeln(foo(1));
end.