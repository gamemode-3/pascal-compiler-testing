program Sample;

var
    score: integer = 78;
    grade: string;

begin
    if score >= 85 then
      grade := 'A'
    else if score >= 75 then
      grade := 'B'
    else if score >= 65 then
      grade := 'C'
    else if score >= 50 then
      grade := 'D'
    else
      grade := 'F';
    
    writeln('The grade is:');
    writeln(grade);
end.