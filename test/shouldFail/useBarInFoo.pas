program Sample;

function foo(x : integer) : integer;
begin
  foo := bar(x) + 1;
//       ^^^^^^
// Function 'bar' used before it was declared
end;

function bar(x : integer) : integer;
begin
  bar := x + 1;
end;

begin
  writeln(foo(1));
end.
