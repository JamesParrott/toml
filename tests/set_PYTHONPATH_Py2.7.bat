REM Python 2 editable installs don't work very well (becuase of the /src/toml_tools structure?)
REM SETUP Python 2 for venvs on windows
REM py -2 -m ensurepip
REM py -2 -m pip install virtualenv
REM create venv as normal with virtualenv swapped for venv
set PYTHONPATH=%PYTHONPATH%;C:\Users\James\Documents\Coding\repos\toml_tools\src
