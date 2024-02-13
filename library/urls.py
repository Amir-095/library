"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraryapp import views
from libraryapp.views import Search

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('add_book/',views.add_book),
    path('allbook/', views.allbook,name='allbook'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update_book/<book_id>', views.update_book, name='update-book'),
    path('student/',views.studentsignup_view,name='stud-sign'),
    path('studentview/', views.viewstudent_view,name='studentview'),
    path('issuebook/', views.issuebook_view,name='arendabook'),
    path('viewissuedbook/', views.viewissuedbook_view,name='viewissuedbook'),
    path('viewissuedbookbystudent/', views.viewissuedbookbystudent),
    path('delete_issued_book/', views.delete_issued_book, name='delete_issued_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

]
from django.conf.urls.static import static
from django.conf import settings
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)