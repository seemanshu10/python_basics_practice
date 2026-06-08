@echo off

:: if folder name or directory name contains & and other special symbols 
::python "%~dp0check_render.py" %* 

python  "%~dp0check_render.py" %*
pause