@echo off

del /q Build

echo %cd%

7z a -tzip Build/IndustrialDestiny ./IndustrialDestiny/*

pause