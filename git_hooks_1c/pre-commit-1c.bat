@echo off
workon git-hooks-1c
for %%i in (gh1c.exe) do "%%~$Path:i pre_commit"
deactivate
