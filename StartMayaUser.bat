@echo off


IF "%PROJECT_BOREALIS_ASSETS%" == "" (
    goto get_asset_dir
) ELSE (
    set assets_dir=%PROJECT_BOREALIS_ASSETS%
    goto set_module_path
)

:get_asset_dir
SET /p assets_dir="Path to the raw-assets folder: "

IF EXIST %assets_dir% (
    SETX PROJECT_BOREALIS_ASSETS "%assets_dir%"
    goto set_module_path
) ELSE (
    echo Invalid path
    goto get_asset_dir
)


:set_module_path
set ToolsPath=%cd%
set MAYA_MODULE_PATH=%ToolsPath%

git pull

for /f "tokens=2*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\2019\Setup\InstallPath" /v MAYA_INSTALL_LOCATION') do set "MayaInstallDir=%%~b"
cd /d %MayaInstallDir%
start bin\maya.exe -proj "%assets_dir%"