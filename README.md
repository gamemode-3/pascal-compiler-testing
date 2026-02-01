# pascal-compiler-testing
Meine Test Cases plus ein Skript mit dem alle Tests ausgeführt werden

## Voraussetzungen
Für die Liveness-Tests braucht ihr nur [Python](https://www.python.org/).

Linux (Debian / Ubuntu):
```bash
sudo apt install python3
```

Für die Kompilierungs-Tests müsst ihr auch noch [FPC](https://www.freepascal.org/) (Free Pascal Compiler 3.2.2) installiert haben.

Linux (Debian / Ubuntu):
```bash
sudo apt install fpc
```

## Einstellungen
Ihr werdet eure Aufrufsyntax evtl. noch einfügen müssen. Dazu gibt es am Anfang der `test_compiler.py`-Datei die Konstante `OWN_COMPILE_CMD`.


## Tests ausführen
### Kompilier-Tests
Einen Test (Gibt Details aus):
```
python3 test_compiler.py <test_case>
```

Alle Tests (Gibt keine Details aus):
```
python3 test_compiler.py -a [<test_dir>]
```
Wenn `<dir>` ausgelassen wird, wird ./test/ verwendet.

Alle Pascal-Dateien in dem angegebenen Ordner und allen Unterordnern werden getestet. Ordner und Dateien, die mit `_` oder `-` beginnen werden ignoriert, sowie sample.pas

### Liveness
Einen Test:
```
python3 test_compiler.py -l <test_case>
```

Alle Tests:
```
python3 test_compiler.py -l -a [<test_dir>]
```
Wenn `<dir>` ausgelassen wird, wird ./test/liveness verwendet.


## Beispielausgabe mit `-a`
<img width="1747" height="484" alt="image" src="https://github.com/user-attachments/assets/f62cb661-71df-482b-a9dc-d0fdb0c744b1" />

## Beispielausgabe ohne `-a`
<img width="1747" height="1147" alt="image" src="https://github.com/user-attachments/assets/935b4aad-1a93-4126-8c9c-a7f7e437defb" />

## Credits
Einige der Test Cases sind von [Jonas' Repo](https://codeberg.org/jfowl/CoBa2025-Pacal-Test-Cases) übernommen (und leicht abgewandelt)
