from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('all_books/', views.AllBooks.as_view(), name='all_books'),
    path('update_book/<int:pk>', views.UpdateBook.as_view(), name='update_book'),
    path('delete_book/<int:pk>', views.DeleteBook.as_view(), name='delete_book'),
    path('staff_dashboard/', views.StaffDashboard.as_view(), name='staff_dashboard'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('student_dashboard/', views.StudentDashboard.as_view(), name='student_dashboard'),
    path('all_books_for_student/', views.AllBooksForStudent.as_view(), name='all_books_for_student'),      
]


    