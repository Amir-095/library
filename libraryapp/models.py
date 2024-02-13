from django.db import models
#таблица для книг
class Book(models.Model):
    Fantastic='Фантастика'
    Biography='Биография'
    Apocalips='Апокалипсис'
    Detective='Детектикв'
    Category_spisok=[
        (Fantastic,'Фантастика'),
        (Biography, 'Биография'),
        (Apocalips, 'Апокалипсис'),
        (Detective, 'Детектив'),
    ]
    name=models.CharField(max_length=200)
    avtor_name=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=Category_spisok,default=Fantastic)
    image=models.ImageField(upload_to='images')
    izdatelstvo=models.CharField(max_length=200,default='')
    description=models.CharField(max_length=2000,default='')
    vozrast = models.CharField(max_length=10, default='')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'

##new
from django.contrib.auth.models import User
#таблица для студента
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomer = models.IntegerField(default=0)
    def __str__(self):
        return self.user.first_name +' '+ self.user.last_name+'['+str(self.nomer)+']'
    #Функция для получения имени студента
    def get_name(self):
        return self.user.first_name

    # Функция для получения имени и фамилии студента
    def get_full_name(self):
        return self.user.first_name+' '+self.user.last_name

    # Функция для получения фамилии студента
    def get_surname(self):
        return self.user.last_name
##new
from datetime import datetime,timedelta


# Получение даты для возвращения книги
def get_expiry():
    return datetime.today() + timedelta(days=14)

#Таблица для выдачи книг
class IssuedBook(models.Model):
    nomer=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.nomer