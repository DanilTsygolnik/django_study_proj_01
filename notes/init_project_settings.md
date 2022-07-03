## Добавление приложения в проект

Находимся в директории `website_root`:
```
(django_env)$ python manage.py startapp pages
```

Прописываем созданное приложение в настройках проекта отдельной строчкой (файле `website/settings.py`):
```python
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    ...
]
```

Что за строчка? - Название класса из файла `pages/apps.py`:
```python
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
```

## Моделирование данных HTML-страниц

Модель - класс в файле `website_root/pages/models.py`.

Каждая статическая страница имеет следующие уникальные элементы:
- заголовок или `title`;
- адрес или `permalink`;
- содержимое веб-страницы или `body_html`;

Отдельные страницы можно представить в виде строк таблицы в БД, где каждому свойству будет соответствовать отдельный столбец (поле) с определённым типом данных. Их также нужно продумать:
- заголовок и адрес -- тип `CharField` для строк небольшой длины;
- текст на странице -- тип `TextField` для большого кол-ва текста.

Модель в Django - представление данных в БД, как класса (таблица) и атрибутов (полей):
```python
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    body_html = models.TextField('Page Content', blank=True)
```
Наследование от класса `Model` из модуля `django.db/models.py`. Типы данных оттуда же?

Замечания по атрибутам:
- `permalink` должно быть уникальным, поэтому в параметрах `unique=True`;

Добавляем метода класса `__str__(self)`, чтобы выводить заголовки? Что именно делает метод?


После создания модели делаем миграции, чтобы добавить её в БД.

```
python manage.py makemigrations
python manage.py migrate
```

[gitignore for django](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) и[почему нужно добавлять migrations в коммиты](https://stackoverflow.com/questions/28035119/should-i-be-adding-the-django-migration-files-in-the-gitignore-file) 

## Добавить модели через API

Написал скрипт -- вставить

Результат:
```
>>> exec(open('add_models_to_db.py').read())
>>> Page.objects.all()
<QuerySet [<Page: Home>, <Page: About Us>]>
>>> Page.objects.get(pk=1)
<Page: Home>
>>> Page.objects.get(pk=1).__dict__
{'_state': <django.db.models.base.ModelState object at 0x7ff74f710d90>, 'id': 1, 'title': 'Home', 'permalink': '', 'body_html': 'This is content of Home page'}
>>> Page.objects.get(pk=2).__dict__
{'_state': <django.db.models.base.ModelState object at 0x7ff74f713c40>, 'id': 2, 'title': 'About Us', 'permalink': 'about', 'body_html': 'This is content of About page'}
```


## Добавляем шаблон веб-страниц

Файл с настройками проекта `website_root/website/settings.py`:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'website/templates')],
        'APP_DIRS': True,
        ... }]
```

Именно `'DIRS': [os.path.join(BASE_DIR, 'website/templates')],` - см. dp 122

Создаём директорию для шаблонов -- `mkdir website/templates`

В шаблоне уже предполагается разметка (headers, footers и т.д.), так что нужно сразу подцепить и статические файлы.

В том же файле настроек, но уже в подвале дописываем:
```python
STATIC_URL = 'static/'
STATICFILES_DIR = [os.path.join(BASE_DIR, 'website/static')]
```

Создаём директорию для статических файлов -- `mkdir website/static`

И создаём шаблон `base.html`

Расширяем шаблон для страниц, уже в рамках приложения. Создаём файл `pages/templates/pages/page.html`

## Настройка отображения

Маршрутизация - строка `path('', include(pages.urls)),` в файле `website/urls.py`

Далее создаём `pages/urls.py` и "обрабатываем" пути к home-странице и остальным, генерируемым динамически -- пара строчек, добавить ссылку на файл.

Переходим к файлу `pages/views.py`
