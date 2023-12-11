# building_materials_store
Интернет-магазин стройматериалов

## **Стэк**

Python 3.11  
Django 5.0

## **Как запустить проект:**
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Adelina1231/building_materials_store.git
```

```
cd building_materials_store/
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
. venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:
```
py manage.py makemigrations
```

```
py manage.py migrate
```

Создать суперюзера:

```
py manage.py createsuperuser
```
Запустить проект:

```
py manage.py runserver
```

Перейти по ссылке:

```
http://127.0.0.1:8000/admin/
```
