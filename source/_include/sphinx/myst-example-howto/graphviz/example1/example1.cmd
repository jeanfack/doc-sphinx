set SCRIPT_DIR=%~dp0
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

set FILENAME=%~n0

set "DOT_EXE=C:\Program Files\Graphviz\bin\dot.exe"

"%DOT_EXE%" -Tsvg -o "%SCRIPT_DIR%\%FILENAME%.svg" "%SCRIPT_DIR%\%FILENAME%.dot"
