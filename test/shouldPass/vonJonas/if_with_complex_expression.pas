program ifWithComplexExpression;
begin
    if ( (3 + 4 > 5) and (not (2 = 3)) or false or (true = (3 <> 3)) ) then
    begin
        writeln('Condition is true');
    end
    else
    begin
        writeln('Condition is false');
    end;
end.