@echo off
if exist "D:\Python3_9\python.exe" (
    echo Python Executable found. Running the script...
    "D:\Python3_9\python.exe" "D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\10_Batch(.bat) Files\CP\script.py"
)else (
    echo Python Excecutable not found at the specified path.
)
pause