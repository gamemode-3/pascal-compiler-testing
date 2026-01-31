program Sample;

function foo(x : integer) : integer;
begin
  foo := foo(x) - 1; // compiles, even though it would infinitely recurse
end;

begin
  writeln(foo(1));
end.
