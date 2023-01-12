@ECHO OFF

::Set the path and file name that we want to save our data in
set filename=c:\stefan\test.txt

::Obtain the data with Windows Commands
for /f "tokens=1-3 delims=//" %%a in ('date /t') do (set datestamp=%%a/%%b/%%c)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set timestamp=%%a:%%b)

::Write the data to a file
echo On the %datestamp%at %timestamp% this information was found: >> %filename%
systeminfo | findstr Available | findstr Physical >> %filename%

::pause