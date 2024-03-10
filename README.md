# Тема проекта(library)
Система учета библиотечных ресурсов и книг: хранение информации о книгах, авторах, категориях и доступных экземплярах; организация системы выдачи книг, учет сроков и возврата; онлайн-каталог, регистрация читателей и учет действий в библиотеке.
# Установка проекта
1. Скопируйте репозиторий:
2. git clone https://github.com/Amir-095/library.git
3. cd library
4. Установите необходимые библиотеки:
5. pip install -r requirements.txt
6. Создайте базу данных PostgreSQL и обновите DATABASES в файле settings.py.
7. DATABASES = { <br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'your_database_name',<br/>
        'USER': 'your_database_user',<br/>
        'PASSWORD': 'your_database_password',<br/>
        'HOST': '127.0.0.1',<br/>
        'PORT': '5432',<br/>
    }<br/>
 }<br/>
10. Выполните миграций:
11. python3 manage.py makemigrations
12. python3 manage.py migrate
13. Запустите проект:
14. python3 manage.py runserver
# Дополнительная информация
Для создания аккаунта администратора библиотеки , создайте superuser-а через терминал.
При загрузке фотографии для обложки книги, в папке проекта автоматически создается папка media в котором хранятся эти фотографии.
