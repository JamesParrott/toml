@ECHO OFF
REM https://stackoverflow.com/a/4580120/20785734
REM Usage: toml-test .\tests\decoding_test.bat -skip invalid
setlocal
set PYTHONPATH=%~dp0\..\src
py -3 decoding_test.py
endlocal


