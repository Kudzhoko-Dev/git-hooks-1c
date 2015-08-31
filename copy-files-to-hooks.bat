@echo off
xcopy "%~dp0pre-commit" ".git/hooks" /F /Y
xcopy "%~dp0pre-commit-1c.py" ".git/hooks" /F /Y
xcopy "%~dp0pre-commit-1c.ini" ".git/hooks" /F /Y
git config --local core.quotepath false