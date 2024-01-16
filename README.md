## Домашка пятая
### Пути для создания и просмотра платежей:
    payments/course/<course:pk>/create/, оплата курса
    payments/lesson/<lesson:pk>/create/, оплата урока
    payments/course/<payment:pk>/retrieve/, просмотр оплаты курса
    payments/lesson/<payment:pk>/retrieve/, просмотр статуса оплаты урока
                         
### Отчёт по тестированию в файле
    ./report_test.txt
### В папке fixtures сохранены фикстуры для приложений lms_app(курсы и уроки) и payments.
### Есть возможность создавать суперпользователя кастомной командой 
    python manage.py csu
### Есть возможность создать обычного пользователя кастомной командой 
    python manage.py create_simple_user

