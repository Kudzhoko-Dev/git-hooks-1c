Утилита для автоматической разборки *epf*-, *erf*-, *md*- и *ert*-файлов при помещении (committing) в git-репозиторий
===

Что делает
---

*epf*- и *erf*-файлы автоматически разбираются с помощью [v8Reader](https://github.com/xDrivenDevelopment/v8Reader), а 
*md*-и *ert*-файлы — с помощью [GComp](http://1c.alterplast.ru/gcomp/). Результат разбора добавляется в индекс и 
помещается в git-репозиторий.

*create-links-in-hooks.bat* (или *copy-files-to-hooks.bat*, если вдруг создание символических ссылок невозможно) нужно 
запускать из каталога проекта.

Требования
---

- Windows
- Python 3.5. Каталог интерпретатора Python должен быть прописан в переменной окружения Path
- Пакет [decompiler1cwrapper](https://github.com/Cujoko/decompiler1cwrapper) с необходимыми настройками
- В переменной окружения Path должен быть прописан каталог *githooksfor1c*
- Платформа 1С:Предприятие 8.3
- Сервисная информационная база (в которой будет запускаться *V8Reader.epf*)
- [v8Reader](https://github.com/xDrivenDevelopment/v8Reader)
- [GComp](http://1c.alterplast.ru/gcomp/)

Состав
---

- *precommit1c.py* — cобственно скрипт
- *pre-commit.sample* — образец hook-скрипта, запускающего *pre-commit-1c.bat*
- *pre-commit-1c.bat* — *bat*-скрипт, ищущий в переменной окружения Path путь до *precommit1c.py* и запускающий его
- *create-links-in-hooks.bat* — *bat*-скрипт, создающий символические ссылки в *.git/hooks* проекта на 
*pre-commit.sample* (c именем *pre-commit*) и *pre-commit-1c.bat*
- *copy-files-to-hooks.bat* — *bat*-скрипт, копирующий в *.git/hooks* проекта *pre-commit.sample* (под именем 
*pre-commit*) и *pre-commit-1c.bat*