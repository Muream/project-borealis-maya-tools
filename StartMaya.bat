@echo off

set ToolsPath=%cd%
SET MAYA_MODULE_PATH=%ToolsPath%

REM git pull

for /f "tokens=2*" %%a in ('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\2019\Setup\InstallPath" /v MAYA_INSTALL_LOCATION') do set "MayaInstallDir=%%~b"
cd /d %MayaInstallDir%
Start bin\maya.exe