program Sample;

function foo(x : integer) : integer;
begin
  foo := x - 1;
end;

function bar(x : integer) : integer;
begin
  bar := foo(x) - 1; // works because foo is declared before bar
end;

begin
  writeln(foo(1));
end.
