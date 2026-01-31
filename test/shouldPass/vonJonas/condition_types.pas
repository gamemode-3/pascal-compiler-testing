program ConditionTypes;
begin
    if ((true = false) or (false <> true)) then
    begin
        writeln('Boolean condition met');
    end;
    
    if ((1 <> 2) or (3 > 4) or (4 >= 3) or (3 < 245) or (2 <= 3) or (42 = 42)) then
    begin
        writeln('Integer condition met');
    end;

    if ((3.14 <> 2.71) or (1.0 > 0.0) or (2.0 >= 2.0) or (0.0 < 1.0) or (3.0 <= 4.0) or (1.618 = 1.618)) then
    begin
        writeln('Double condition met');
    end;

    if (('CoBa1' <> 'CoBa2') or ('pascal' = 'pascal')) then
    begin
        writeln('String condition met');
    end;

    if ((true and (1 < 2)) or ((3.14 >= 2.71) and ('a' = 'a'))) then
    begin
        writeln('Mixed condition met');
    end;
end.