@echo off
mklink ".git/hooks/pre-commit" "%~dp0pre-commit.sample"
mklink ".git/hooks/pre-commit-1c.bat" "%~dp0pre-commit-1c.bat"
git config --local core.quotepath false
