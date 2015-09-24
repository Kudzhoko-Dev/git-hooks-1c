Утилита для автоматической разборки *epf*-, *erf*-, *md*- и *ert*-файлов при помещении (committing) в git-репозиторий
===

Что делает
---

*epf*- и *erf*-файлы автоматически разбираются с помощью [v8Reader](https://github.com/xDrivenDevelopment/v8Reader), а 
*md*-и *ert*-файлы — с помощью [GComp](http://1c.alterplast.ru/gcomp/). Результат разбора добавляется в индекс и 
помещается в git-репозиторий.

Пути к платформе 1С:Предприятие 8, сервисной информационной базе, *V8Reader.epf* и GComp указывается в файле настроек 
*pre-commit-1c.ini*, который сначала ищется в каталоге проекта, а затем в каталоге с *pre-commit-1c.py*.

*create-links-in-hooks.bat* (или *copy-files-to-hooks.bat*, если вдруг создание символических ссылок невозможно) нужно 
запускать из каталога проекта.

Требования
---

- Windows
- Python 3.4. Путь до *python.exe* должен быть прописан в переменной окружения Path
- В переменной окружения Path должен быть прописан путь до *pre-commit-1c.py*
- Платформа 1С:Предприятие 8.3
- Сервисная информационная база (в которой будет запускаться *V8Reader.epf*)
- [v8Reader](https://github.com/xDrivenDevelopment/v8Reader) и в частности *V8Reader.epf*
- [GComp](http://1c.alterplast.ru/gcomp/)

Состав
---

- *pre-commit-1c.py* — cобственно скрипт
- *pre-commit-1c.ini.sample* — образец файла с настройками
- *pre-commit.sample* — образец hook-скрипта, запускающего *pre-commit-1c.bat*
- *pre-commit-1c.bat* — *bat*-скрипт, ищущий в переменной окружения Path путь до *pre-commit-1c.py* и запускающий его
- *create-links-in-hooks.bat* — *bat*-скрипт, создающий символические ссылки в *.git/hooks* проекта на 
*pre-commit.sample* (c именем *pre-commit*) и *pre-commit-1c.bat*
- *copy-files-to-hooks.bat* — *bat*-скрипт, копирующий в *.git/hooks* проекта *pre-commit.sample* (под именем 
*pre-commit*) и *pre-commit-1c.bat*