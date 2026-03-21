@echo off
echo Preparing to launch tools...
timeout 3

set NUKE_PATH="C:\Program Files\Nuke\Nuke.exe"
set MAYA_PATH="c:\Program Files\Autodesk\Maya2022\bin\maya.exe"
set HOUDINI_PATH="C:\Program Files\Houdini\Houdini.exe"
set NOTEPAD_PATH="c:\Windows\system32\notepad.exe"
if exist "%HOUDINI_PATH%" (
    start "" "%HOUDINI_PATH%"
)

if exist "%NUKE_PATH%"" (
    start "" "%NUKE_PATH%"
)

if exist %MAYA_PATH% (
    start "" %MAYA_PATH% 
)
@REM start "" %MAYA_PATH% 

start "" %NOTEPAD_PATH%
echo All Tools launched successfully!
pause