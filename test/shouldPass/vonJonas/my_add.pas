// Taken from the Specification document
program MyAdd;

function MyAdd(a, b: integer): integer;
var
    c: integer;
begin
    c := a + b;
    MyAdd := c;
end;

begin
    writeln(1 + 2);
end.