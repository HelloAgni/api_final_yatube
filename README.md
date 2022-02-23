**API для Yatube**
У неаутентифицированных пользователей доступ к API должен быть только на чтени
Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения
***Установка.***

Клонировать репозиторий и перейти в него:
> git clone ...

Cоздать и активировать виртуальное окружение:
> python3 -m venv env
> source env/bin/activate

Установить зависимости из файла requirements.txt:
> python3 -m pip install --upgrade pip
> pip install -r requirements.txt

Выполнить миграции:
> python3 manage.py migrate

Запустить проект:
> python3 manage.py runserver

**_Примеры._**
```
POST http://127.0.0.1:8000/api/v1/posts/
{
"text": "string",
"image": "string",
"group": 0
}
Response samples 201
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```