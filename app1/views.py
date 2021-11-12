from django.views.generic import CreateView,TemplateView,FormView,ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from .models import Books
from .forms import SignUpForm, BookForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# Home
class Home(TemplateView):
    template_name = 'app1/home.html'

# Staff signup 
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'app1/signup.html' 
    success_url = '/login/'

# Staff Login
class Login(LoginView,FormView):
    template_name = 'app1/login.html' 
    success_url = '/staff_dashboard/' 

# Staff Dashboard
@method_decorator(staff_member_required, name='dispatch')
class StaffDashboard(TemplateView):
    template_name = 'app1/staff_dashboard.html'

# Add New Book
@method_decorator(staff_member_required, name='dispatch')
class AddBook(CreateView):
    form_class = BookForm
    template_name = 'app1/add_book.html'
    success_url = '/add_book/'

# Retrieve all Books
@method_decorator(staff_member_required, name='dispatch')
class AllBooks(ListView):
    model = Books
    template_name = 'app1/all_books.html'
    context_object_name = 'data'

# Update Book
@method_decorator(staff_member_required, name='dispatch')
class UpdateBook(UpdateView):
    model = Books
    template_name = 'app1/update_book.html'
    fields = ['title', 'author_name','published_date', 'available_status']
    success_url = '/all_books/'

# Delete Book
@method_decorator(staff_member_required, name='dispatch')
class DeleteBook(DeleteView):
    model = Books
    template_name = 'app1/delete_book.html'
    success_url = '/all_books/'

# Logout
class Logout(LogoutView):
    template_name = 'app1/logout.html'



# Student Dashboard
class StudentDashboard(TemplateView):
    template_name = 'app1/student_dashboard.html'

# Student view available Books
class AllBooksForStudent(ListView):
    model = Books
    template_name = 'app1/all_books_for_students.html'
    context_object_name = 'data'
    
