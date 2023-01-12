@ECHO OFF

::Set the path and file name that we want to save our data in
set filename=c:\stefan\test.txt

::Obtain the data with Windows Commands and save to file
date /t >> %filename%
time /t >> %filename%
systeminfo | findstr Available | findstr Physical >> %filename%

pause