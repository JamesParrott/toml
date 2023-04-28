ECHO "Run as admin"
REM BUILD TEST ENV:
REM ipy -X:Frames -m ensurepip 
REM Download, extract and cd into: https://pypi.org/project/ironpython-pytest/#files
REM If you have installed as many packages in Iron Python successfully as I have (zero) it's safe to install globally.
REM ipy -X:Frames -m pip install -e .
REM RUN TESTS: Could clean this up but: 
REM cd into subdir of source to let Iron Python find it.  Or have to create and activate Iron Python venv
cd ..\src
REM run ironpython-pytest, but point back to batch file's dir / test dir
ipy -m pytest ..\tests