
program Variables;

var 
  // Simple declaration:
  Int01: integer;
  Double01: double;
  String01: string;
  Bool01: boolean;

  // Declaration with initialization:
  Int02: integer = 42;
  Int03: integer = -7;
  Double02: double = 3.14;
  Double03: double = -0.001;
  Double04: double = 0;
  String02: string = '';
  Bool02: boolean = true;

begin
  Int01 := 0;
  writeln(Int01);
  Double01 := 0.0;
  writeln(Double01);
  String01 := 'Hello, World!';
  writeln(String01);
  Bool01 := false;
  writeln(Bool01);

  writeln(Int02);
  writeln(Int03);
  writeln(Double02);
  writeln(Double03);
  writeln(Double04);
  writeln(String02);
  writeln(Bool02);
end.
