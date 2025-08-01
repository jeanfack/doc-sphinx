%~d0
cd %~dp0

set SOURCEDIR=source
set BUILDDIR=build-md

sphinx-build -M markdown %SOURCEDIR% %BUILDDIR%
