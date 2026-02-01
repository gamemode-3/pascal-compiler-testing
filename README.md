# pascal-compiler-testing
Meine Test Cases plus ein Skript mit dem alle Tests ausgeführt werden

## Voraussetzungen
Für die Liveness-Tests braucht ihr nur [Python](https://www.python.org/).

Debian / Ubuntu:
```bash
sudo apt install python3
```

Für die Kompilierungs-Tests müsst ihr auch noch [FPC](https://www.freepascal.org/) (Free Pascal Compiler 3.2.2) installiert haben.

Debian / Ubuntu:
```bash
sudo apt install fpc
```

## Einstellungen
Ihr werdet eure Aufrufsyntax evtl. noch einfügen müssen. Dazu gibt es am Anfang der `test_compiler.py`-Datei die Konstante `OWN_COMPILE_CMD`.


## Tests ausführen
### Kompilieren
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
<img width="1377" height="403" alt="image" src="https://github.com/user-attachments/assets/4e03730a-c83c-4b3f-b8e2-74a7280b883c" />

## Beispielausgabe ohne `-a`
<img width="1377" height="965" alt="image" src="https://github.com/user-attachments/assets/86ed74c9-fc74-4ef2-ae1f-23550c4b31ff" />

## Credits
Einige der Test Cases sind von [Jonas' Repo](https://codeberg.org/jfowl/CoBa2025-Pacal-Test-Cases) übernommen (und leicht abgewandelt)
