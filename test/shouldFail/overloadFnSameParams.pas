program Sample;

function foo(x : integer) : integer;
begin
  foo := x - 1;
end;

function foo(x : integer) : integer;
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
// Function 'foo' is already declared with the signature function (x: integer) : integer
begin
  foo := x + 1;
end;

begin
  writeln(foo(1));
end.
