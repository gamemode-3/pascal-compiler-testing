
program DeepNesting;
var
    n : integer;
begin
    n := 10;
    begin
        n := 1;
        begin
            n := 2;
            begin
                begin
                    n := 4;
                    begin
                        n := 5;
                    end;
                end;
                n := 3;
            end;
        end ;
    end;
end.