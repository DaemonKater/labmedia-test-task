# Аналитика платежей. Тестовое задание "Лабмедиа"

## Стек технологий
* **Backend:** Python 3.14, Django 6.0
* **База данных:** PostgreSQL 17
* **Frontend:** Vanilla JS, Bootstrap 5, Chart.js

## Развертывание проекта

### 1. Настройка базы данных и окружения
Создать базу данных в PostgreSQL. Затем создать в корне проекта файл `.env` и указать параметры подключения:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=название_вашей_базы
DB_USER=пользователь_бд
DB_PASSWORD=пароль_от_бд
DB_HOST=127.0.0.1
DB_PORT=5432

2. Установка зависимостей
Создать и активировать виртуальное окружение, затем установить пакеты:

python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

3. Инициализация БД
Применить миграции для создания схемы базы данных:

python manage.py makemigrations
python manage.py migrate

Команда, автоматически заполняющая таблицы тестовыми данными из ТЗ:

python manage.py load_test_data

4. Запуск сервера

python manage.py runserver
Приложение будет доступно по адресу: http://127.0.0.1:8000/