
program Operators;

var 
  int_num : integer = 0;
  double_num : double = 0.0;
  bool_val : boolean = false;
begin
  // All arithmetic operators for integers:
  int_num := 10 + 9 - 8 * 3 + (-4) - (+4);
  writeln(int_num); // -13

  // All arithmetic operators for doubles:
  double_num := 10.0 + 9.0 - 8.0 * (7.0 / 1.0) + (-4.0) - (+4 mod 3);
  writeln(double_num); // -4.2000000000000000E+001

  // All relational and boolean operators:
  bool_val := (int_num = 5) <> (int_num <> 5) And not true Or Not false And (5 > 3) And
              (4  >= 4) And (3 < 5) And (4 <= 4) Or ('' = '') Or ('' <> 'text');
  writeln(bool_val); // TRUE

end.
