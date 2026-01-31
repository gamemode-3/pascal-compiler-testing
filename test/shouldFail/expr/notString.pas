program Sample;
var
  i : string;

begin
  i := not 'hello';
//     ^^^^^^^^^^^
// Unary operator 'not' cannot be applied to string
  writeln(i);
end.
