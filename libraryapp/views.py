from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.generic import ListView
from . import models
#импорты для регистрации и авторизации
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentUserForm,StudentDOPForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#это все

#импорт таблицы с книгами
from .models import Book,Student,IssuedBook
#это все

from django.db.models import Q
from . import forms

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password is incorrect')
    context={}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
#Поиск
class Search(ListView):
    template_name ="index.html"
    context_object_name = ("book")

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        if not query:  # Если запрос пустой
            return redirect('index')  # Перенаправляем на главную страницу
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Book.objects.filter(Q(name__icontains=query) | Q(avtor_name__icontains=query))
        return results

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


from django.contrib.auth.models import Group
#Это регистрация студента, в нем объединяются две формы в одну.
def studentsignup_view(request):
    form = StudentUserForm()
    form2 = StudentDOPForm()

    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        form2 = StudentDOPForm(request.POST)

        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)

            student, created = Student.objects.get_or_create(user=user)
            if created:
                student.save()

            messages.success(request, 'Регистрация успешна.')
            return redirect('login')

    return render(request, 'accounts/studentsignup.html', {'form': form, 'form2': form2})

#new
def viewstudent_view(request):
    students=models.Student.objects.all()
    return render(request,'library/studentview.html',{'students':students})
#new
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    user = student.user
    student.delete()
    user.delete()
    return redirect('studentview')
#операции с книгами
from django.shortcuts import render
from .models import Book
from .forms import BookForm

def add_book(request):
    error_message = None

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']

            # Проверяем, существует ли книга с таким же ISBN
            if Book.objects.filter(isbn=isbn).exists():
                error_message = 'Книга с таким ISBN уже существует'
            else:
                user = form.save()
                return render(request, 'library/bookadded.html')
    else:
        form = BookForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'library/addbook.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def delete_book(request,book_id):
    books=models.Book.objects.get(pk=book_id)
    books.delete()
    return redirect('allbook')

def update_book(request,book_id):
    books = Book.objects.get(pk=book_id)
    form=forms.BookForm(request.POST or None,request.FILES or None , instance=books)
    if form.is_valid():
        form.save()
        return redirect('allbook')
    return render(request,'library/update_book.html',{'books':books,'form':form})

def allbook(request):
    book = Book.objects.all()
    return render(request,'library/allbook.html',{'book':book})
#Конец операции с книгами

def index(request):
    book = Book.objects.all()
    return render(request,'index.html',{'book':book})


from datetime import date
def viewissuedbookbystudent(request):
    student=models.Student.objects.filter(user_id=request.user.id)
    issuedbook=models.IssuedBook.objects.filter(nomer=student[0].nomer)

    li1=[]

    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            t=(book.name,book.avtor_name)
            li1.append(t)
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)

        #Начисление штрафа
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        t=(issdate,expdate,fine)
        li2.append(t)

    return render(request,'library/viewissuedbookbystudent.html',{'li1':li1,'li2':li2})

def issuebook_view(request):
    form = forms.IssuedBookForm()

    if request.method == 'POST':
        form = forms.IssuedBookForm(request.POST)

        if form.is_valid():
            # Получаем выбранного студента и книгу
            student = form.cleaned_data['nomer2']
            book = form.cleaned_data['isbn2']

            # Проверяем, не выдавалась ли уже эта книга студенту
            existing_issue = IssuedBook.objects.filter(nomer=student.nomer, isbn=book.isbn).exists()

            if existing_issue:
                # Добавляем ошибку в форму
                form.add_error(None, 'Эта книга уже выдана этому студенту.')
            else:
                # Создаем новую запись о выдаче
                obj = models.IssuedBook()
                obj.nomer = student.nomer
                obj.isbn = book.isbn
                obj.save()

                return redirect('index')

    return render(request, 'library/issuebook.html', {'form': form})




def viewissuedbook_view(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #Начисление штрафа
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10


        books=list(models.Book.objects.filter(isbn=ib.isbn))
        students=list(models.Student.objects.filter(nomer=ib.nomer))
        i=0
        for l in books:
            t=(students[i].get_full_name,students[i].nomer,books[i].name,books[i].avtor_name,issdate,expdate,fine,books[i].isbn)
            i=i+1
            li.append(t)

    return render(request,'library/viewissuedbook.html',{'li':li})

#Удаление записи
def delete_issued_book(request):
    if request.method == 'POST':
        nomer = request.POST.get('nomer')
        isbn = request.POST.get('isbn')

        try:
            book_to_delete = IssuedBook.objects.get(nomer=nomer, isbn=isbn)
        except IssuedBook.DoesNotExist:
            return HttpResponse("Книга с таким номером и ISBN не найдена.")
        except Exception as e:
            return HttpResponse(f"Произошла ошибка: {str(e)}")
        book_to_delete.delete()
    return redirect('viewissuedbook')
