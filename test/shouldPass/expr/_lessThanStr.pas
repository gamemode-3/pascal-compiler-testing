program Sample;
var
  i : boolean = false;

begin
  i := 'aa' < 'ab'; // compares string lexicographically ('a' < 'b' < 'c' < ...; 'a' < 'aa')
end.
