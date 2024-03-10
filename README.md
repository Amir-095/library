# Тема проекта(library)
Система учета библиотечных ресурсов и книг: хранение информации о книгах, авторах, категориях и доступных экземплярах; организация системы выдачи книг, учет сроков и возврата; онлайн-каталог, регистрация читателей и учет действий в библиотеке.
# Установка проекта
1. Скопируйте репозиторий:
```
 git clone https://github.com/Amir-095/library.git
 cd library
```
2. Установите необходимые библиотеки:
```
 pip install -r requirements.txt
```
3. Создайте базу данных PostgreSQL и обновите DATABASES в файле settings.py.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
4. Выполните миграций:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Запустите проект:
```
python3 manage.py runserver
```
# Дополнительная информация
Для создания аккаунта администратора библиотеки , создайте superuser-а через терминал.
При загрузке фотографии для обложки книги, в папке проекта автоматически создается папка media в котором хранятся эти фотографии.
