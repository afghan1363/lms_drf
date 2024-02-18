## Домашка четвёртая
### Используется виртуальное окружение VENV
### Чтобы развернуть проект необходимо выполнить следующие действия:
### Клонировать репозиторий.
### Активировать виртуальное окружение
    source env/bin/activate.bat
### Установить зависимости 
    pip3 install -r requirements.txt
### Создать файл 
    .env
### Заполнить его данными из файла
    env.sample
### Создать базу данных в PostreSQL
    atomic_habits
### Создать миграции командой
    python3 manage.py makemigrations
### И применить миграции
    python3 manage.py migrate
    
## Документация
### Документация для API реализована посредством drf-yasg и доступна по следующим эндпоинтам:
    http://127.0.0.1:8000/redoc/
    http://127.0.0.1:8000/swagger/
### Для проекта настроена DOCKER контейниризация, что позволяет его развернуть в изолированной docker - системе
### Для упаковки проекта использовать комманду
    docker compose build
### Для запуска
    docker compose up
### Веб приложение будет доступно по адресу
    http://127.0.0.1:8001/
### Документация
    http://127.0.0.1:8001/redoc/
    http://127.0.0.1:8001/swagger/
### Отчёт по тестированию в файле
    ./report_test.txt
### В папке fixtures сохранены фикстуры для приложений lms_app(курсы и уроки) и payments.
### Есть возможность создавать суперпользователя кастомной командой 
    python manage.py csu
### Есть возможность создать обычного пользователя кастомной командой 
    python manage.py create_simple_user

