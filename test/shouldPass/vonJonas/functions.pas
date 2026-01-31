
program Functions;

Procedure proc1();
begin
  writeln('proc1');
end;

procedure proc2(a : integer);
begin
  writeln('proc2');
end;

function fn1() : boolean;
begin
  proc1();
  // no return value
  fn1 := true;
end;

Function fn2(a, b : integer) : integer;
begin
  fn2 := a + b;
end;

Function fn3(a : integer; b : integer) : boolean;
begin
  fn3 := a = b;
end;

Function fn4(a : double; b : double) : double;

var 
  result : double;
begin
  result := a + b;
  fn4 := result;
end;

begin
  fn1();
  proc2(2);
  writeln( fn2(1, 2) );
  writeln( fn3(42, 42) );
  writeln( fn4(1.2, 3.4) );
end.
