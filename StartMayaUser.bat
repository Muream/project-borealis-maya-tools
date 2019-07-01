@echo off

set ToolsPath=%cd%
set MAYA_MODULE_PATH=%ToolsPath%

git pull

for /f "tokens=2*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\2019\Setup\InstallPath" /v MAYA_INSTALL_LOCATION') do set "MayaInstallDir=%%~b"
cd /d %MayaInstallDir%
start bin\maya.exe