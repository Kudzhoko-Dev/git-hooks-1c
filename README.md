Набор утилит для перехватчиков (hooks) Git
===

Что делает
---

Смотри Состав 

Требования
---

- Windows
- Python 3.5. Каталоги интерпретатора и скриптов Python должны быть прописаны в переменной окружения Path
- Пакет [decompiler1cwrapper][1] с необходимыми настройками

Состав
---

- *precommit1c.py* — скрипт для разборки *epf*-, *erf*-, *ert*- и *md*-файлов с помощью пакета 
[decompiler1cwrapper][1] в каталоги, которые затем добавляются в индекс и 
помещаются (committing) в git-репозиторий
- *pre-commit.sample* — образец hook-скрипта, запускающего *pre-commit-1c.bat*
- *pre-commit-1c.bat* — *bat*-скрипт, ищущий в переменной окружения Path путь до *precommit1c.exe* и запускающий его
- *createlinksinhooks.py* — скрипт, создающий символические ссылки (только для Windows Vista и выше для пользователей
и групп пользователей в локальной групповой политикой "Create Symbolic Links" в
"Computer Configuration\Windows Settings\Local Policies\User Rights Assignment") в *.git/hooks* проекта на
*pre-commit.sample* (c именем *pre-commit*) и *pre-commit-1c.bat*

Установка
---

Вы можете собрать пакет, запустив *setup.py* с ключом sdist. После чего в каталоге *dist* проекта появится *zip*-архив
пакета, установить который можно запустив:

> pip install <архив>

После установки в каталоге скриптов интерпретатора Python появится файл *clihp.exe*, который предназначен для быстрого
создания в каталоге *.git\\hooks* репозитория символических ссылок на необходимые для работы утилиты файлы. Запускать
его нужно из каталога репозитория.

[1]: https://github.com/Cujoko/decompiler1cwrapper
