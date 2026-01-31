program Sample;
var
  i : boolean = false;

begin
  i := 1.0 < 3;
  i := 1 < 3.0;
  writeln(i);
end.
