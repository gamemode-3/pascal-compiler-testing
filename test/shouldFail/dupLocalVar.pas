program Sample;

function foo(): integer;
var
  b : integer;
  b : integer;
//^
// Symbol 'b' is already declared in this scope
begin
  foo := b;
end;

begin
  writeln(foo());
end.
