set SCRIPT_DIR=%~dp0
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%


::set DOT_EXE=C:\ProgramData\anaconda3\Library\bin\dot.exe
set DOT_EXE=C:\Program Files\Graphviz\bin\dot.exe

"%DOT_EXE%" -Tsvg -o "%SCRIPT_DIR%\example.svg" "%SCRIPT_DIR%\example.dot"

::dot.bat -Tsvg -O %SCRIPT_DIR%\example.dot
