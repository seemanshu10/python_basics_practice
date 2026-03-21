@echo off

set batchFolder=%~dp0
@REM echo Batch file is in: %batchFolder%

@REM echo Accessing Python Script:
@REM python "%batchFolder%myscript.py"

@REM echo Accessing Asset File:
@REM echo Asset path: "%batchFolder%..\assets\texture.png"

echo Opening Asset File:
set imagePath=%batchFolder%..\assets\texture.png
echo Asset path: "%imagePath%"

start "" "%imagePath%"

pause



