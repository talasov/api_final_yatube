# API для Yatube
____
Учебный проект Яндекс.Практикум

## Описание
____
>Yatube - социальная сеть для публикации дневников. Позволяет публиковать посты, комментировать посты, осуществлять подписку на авторов.

Для разработки API использован Django REST Framework.

## Установка и запуск
____
1. Перейдите в папку yatube_api (cd yatube_api)
2. Установите виртуальное окружение (python -m venv venv)
3. Активируйте виртуальное окружение (source venv/Scripts/activate)
4. Установите зависимости из файла requirements.txt (pip install -r requirements.txt)
5. Выполните миграции (python manage.py migrate)
6. Запустите проект (python manage.py runserver)


## Документация к API
____

После запуска dev-сервера документация к API доступна по адресу: http://127.0.0.1:8000/redoc/
