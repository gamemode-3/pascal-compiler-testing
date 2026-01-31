program Sample;
var
  x: integer;
  y: double;
begin
  writeln(x mod y);
//        ^^^^^^^
// Operator 'mod' cannot be applied to integer and double
end.
