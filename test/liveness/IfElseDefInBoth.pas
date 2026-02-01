program IfElseDefInBoth;

var
    a, b: integer;
    c: string;

begin
    c := 'unused :o'; //    out | in
    b := 10; //               b | 
    writeln(b); //               | b
    a := 4; //                a |
    if a < 2 then //            | a
        c := 'c :D' //          | c
    else
        c := 'also c :D'; //    | c
    writeln(c) //             c |
end.

// [[LIVENESS_REGISTERS:1]]