program Sample;
var
  a: integer;
  b: integer;
  c: integer;
  d: integer;

begin
  a := 5;
  
  if true then begin
    b := 1;
    c := a;
    a := b + 1;
  end else begin
    b := 1;
  end;

  writeln(a);
end.