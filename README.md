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
3. Создайте базу данных PostgreSQL, после создайте файл .env и введите туда эти данные
```
POSTGRES_DB = Database name
POSTGRES_US = Username
POSTGRES_PASSWORD = Your postgres password
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
