pushd "%~dp0"

%~d0
cd %~dp0
call make.bat clean

popd
