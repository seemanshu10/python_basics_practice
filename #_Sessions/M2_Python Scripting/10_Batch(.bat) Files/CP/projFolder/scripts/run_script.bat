@echo off

set basepath=%~dp0

::echo Base Path : %basepath%
set config_path=%basepath%..\config.cfg
echo %config_path%
python "%basepath%myScript.py" "%basepath%..\config.cfg"
pause