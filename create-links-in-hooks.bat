@echo off
mklink ".git/hooks/pre-commit" "%~dp0pre-commit.sample"
mklink ".git/hooks/pre-commit.bat" "%~dp0pre-commit.bat"
git config --local core.quotepath false
