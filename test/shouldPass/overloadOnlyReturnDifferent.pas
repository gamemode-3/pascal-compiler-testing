program Sample;

function foo(x : integer) : integer;
begin
  foo := x + 1;
end;

function foo(x : integer) : boolean;
begin
  foo := x = 2;
end;

begin
  writeln(foo(1)); // First overload is chosen.
end.
