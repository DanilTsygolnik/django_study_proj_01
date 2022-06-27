## Создание проекта

Инициализация проекта внутри git-репозитория в директории website:
```
(django_env)$ django-admin startproject website
```
Для удобства ориентирования переименовываем директорию с настройками сайта и переходим в неё для дальнейшей работы:
```bash
mv website/ website_root/
cd website_root/
```
Последний шаг первичной настройки - применить [миграции](note_on_migrations.md):
```
python manage.py migrate
```
Структура только что созданного проекта:
```
website_root/
├── website/
│   ├── __pycache__/
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

Запускаем сервер на localhost'e:
```
python manage.py runserver
```

Убеждаемся, что все работает, открыв нужный адрес в веб-браузере (например, Firefox):
```
firefox http://127.0.0.1:8000/
```

<img src="https://docs.docker.com/samples/images/django-it-worked.png" height=200>
