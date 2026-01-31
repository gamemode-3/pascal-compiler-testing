// Taken from the Specification document
program Fibonacci;

function Fib ( n : integer ) : integer ;
begin
    if ( n > 0 ) then
        if ( n <= 2 ) then
            Fib := 1
        else
            Fib := Fib ( n-1 ) + Fib ( n-2 )
    else
        Fib := 0
end;

begin
    writeln ( Fib ( 5 ) ) ;
    writeln ( Fib ( 10 ) ) ;
end.