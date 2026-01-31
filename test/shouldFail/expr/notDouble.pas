program Sample;
var
  i : double;

begin
  i := not 10.0;
//     ^^^^^^^^
// Unary operator 'not' cannot be applied to double
  writeln(i);
end.
