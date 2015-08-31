@echo off
mklink ".git/hooks/pre-commit" "%~dp0pre-commit"
mklink ".git/hooks/pre-commit-1c.py" "%~dp0pre-commit-1c.py"
mklink ".git/hooks/pre-commit-1c.ini" "%~dp0pre-commit-1c.ini"
git config --local core.quotepath false