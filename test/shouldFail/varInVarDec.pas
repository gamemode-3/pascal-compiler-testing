program Sample;
var
 i : integer = 0;
 x : integer = i + 1;
//             ^
// Variables can not be used in variable declarations

begin
  writeln(x);
end.
