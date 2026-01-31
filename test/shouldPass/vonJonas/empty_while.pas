// Apparently, this is allowed by the FPC compiler:
// -------------------------------------------------------------
//  $ fpc examples/parsable/empty_while.pas 
//  Free Pascal Compiler version 3.2.2 [2025/08/02] for x86_64
//  Copyright (c) 1993-2021 by Florian Klaempfl and others
//  Target OS: Linux for x86-64
//  Compiling examples/parsable/empty_while.pas
//  empty_while.pas(17,1) Warning: unreachable code
//  Linking examples/parsable/empty_while
//  17 lines compiled, 0.1 sec
//  1 warning(s) issued
// -------------------------------------------------------------
program EmptyWhile;
begin
 while(true and false)
 do
end.
