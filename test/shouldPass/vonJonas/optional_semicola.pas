
program OptionalSemicola;
begin

  // if-else statements:
  if true then
    writeln('None needed')
  else
    writeln('But possible');

  // Empty block ok:
  begin
  end;

  // Single-statement block:
  begin
    writeln('Optional, as only statement in block')
  end;

  // Multi-statement block:
  begin
    writeln('Required');
    writeln('As multiple statements in block');
  end;

  //while-loops:
 while false do
    writeln('Also none needed')
  ;
  // ends the while-block

 while false do
    begin
      writeln('Also none needed')
    end;

 while false do
    begin
      writeln('Needed');
      writeln('Needed');
    end;

end.
