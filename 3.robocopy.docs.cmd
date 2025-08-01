set SCRIPT_DIR=%~dp0
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

set SRC=%SCRIPT_DIR%\build\html
set DST=%SCRIPT_DIR%\docs

robocopy.exe "%SRC%" "%DST%" /MIR /NP /R:10
