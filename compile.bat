@echo off 
title CTSHELL
color 3 
cls 
chcp 65001 
echo.
echo                      _             
echo                  ___| |___   _____ 
echo                 / __| __\ \ / / __|
echo                | (__| |_ \ V /\__ \
echo                 \___|\__| \_/ |___/
echo. 
echo.                                                        
set /p choice= Are you sure you want to compile your Client (Yes / No) 
if "%choice%"=="Yes" goto compile
if "%choice%"=="No" goto bye
:compile
pyinstaller client.py --onefile
del client.spec
cd dist 
explorer .\
cls
echo compiled 
:bye 
exit 
