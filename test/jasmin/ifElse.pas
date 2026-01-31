program Sample;
var
  a: integer;

begin
  a := 5;
  
  if a > 3 then
    a := a + 1;

  if a > 3 then
    a := a + 1
  else
    a := a - 1;

  writeln(a);
end.