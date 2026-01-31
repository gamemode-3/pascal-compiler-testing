program Sample;
var
  x : integer;

begin
  x := 10 / 32;
//     ^^^^^^^
// Cannot assign double to integer
  writeln(x);
end. 