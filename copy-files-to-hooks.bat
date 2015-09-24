@echo off
xcopy "%~dp0pre-commit.sample" ".git/hooks/pre-commit" /F /Y
xcopy "%~dp0pre-commit-1c.bat" ".git/hooks" /F /Y
git config --local core.quotepath false
