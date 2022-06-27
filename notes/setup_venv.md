## Настройка окружения в UNIX-подобных ОС

В ОС должен быть установлен Python версии 3.3+, тогда не потребуется отдельная устанавка пакета [python-virtualenv](https://archlinux.org/packages/?name=python-virtualenv).

Убеждаемся в наличии интерпретатора Python и менеджера пакетов:
```
$ python3 --version
Python 3.10.4

$ python3 -m venv --help
usage: venv ...

$ pip3 --version
pip 22.1.1 from /home/username/.local/lib/python3.10/site-packages/pip (python 3.10)
```

Перед работой с виртуальным окружением проводим апргрейд `pip`:[^pip-usage] 
```
$ python3 -m pip install --upgrade pip
```

Создаём виртуальное окружение `django_env`:
```bash
$ python3 -m venv /home/user/path/to/django_env
```

[Если нужно создать виртуальное окружение внутри проекта](venv_inside_the_project.md).

## Установка Django

Установка производится в созданное виртуальное окружение:
```bash
# активируем виртуальное окружение
$ source /absolute/path/to/django_env/bin/activate

# устанавливаем django
(django_env)$ python -m pip install django
```


[^pip-usage]: https://note.nkmk.me/en/python-pip-usage/
