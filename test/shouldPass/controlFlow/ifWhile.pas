program Sample;
var
  x, y: integer;
begin
  y := 1;
  x := 1;
  if x > 0 then
    while y < 10 do
      y := y + 3;
  writeln(y);
end.
