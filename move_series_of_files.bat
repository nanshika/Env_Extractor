@title C:\Script\Util\move_series_of_files.bat
@echo off
copy /Y "%~dp0%~nx0" C:\Script\backup\
setlocal enabledelayedexpansion
pushd C:\data
set STP=100
set CNT=%STP%
for /f "delims=" %%F in ('dir /b /a-d') do (
  set /a QUO=CNT/STP
  set NUM=0000!QUO!
  set NUM=!NUM:~0,5!
  MD !NUM! 2>&1 1>NUL
  move "%%F" !NUM!
  set /a CNT+=1
)
pause
