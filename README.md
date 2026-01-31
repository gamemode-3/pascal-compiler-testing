# pascal-compiler-testing
Meine Test Cases plus ein Skript mit dem alle Tests ausgeführt werden

## Voraussetzungen
Ihr müsst [FPC](https://www.freepascal.org/) (Free Pascal Compiler 3.2.2) installiert haben und [Python](https://www.python.org/).

Debian / Ubuntu:
```bash
sudo apt install fpc python3
```

## Einstellungen
Ihr werdet eure Aufrufsyntax evtl. noch einfügen müssen. Dazu gibt es am Anfang der `test_compiler.py`-Datei die Konstante `OWN_COMPILE_CMD`.


## Ausführen
Einen Test (Gibt Details aus):
```
python3 test_compiler.py <test_case>
```

Alle Tests (Gibt keine Details aus):
```
python3 test_compiler.py -a [<dir>]
```
Wenn `<dir>` ausgelassen wird, wird ./test/ verwendet.

Alle Pascal-Dateien in dem angegebenen Ordner und allen Unterordnern werden getestet. Ordner und Dateien, die mit `_` oder `-` beginnen werden ignoriert, sowie sample.pas

## Credits
Einige der Test Cases sind von [Jonas' Repo](https://codeberg.org/jfowl/CoBa2025-Pacal-Test-Cases) übernommen (und leicht abgewandelt)