from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('add_course',views.add_course,name='add_course'),
    path('add_course1',views.add_course1,name='add_course1'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
    path('add_studentdb',views.add_studentdb,name='add_studentdb'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_db/<int:pk>',views.edit_db,name='edit_db'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('add_teacherdb',views.add_teacherdb,name='add_teacherdb'),
    path('show_teacher',views.show_teacher,name='show_teacher'),
    path('th_delete/<int:pk>',views.th_delete,name="th_delete"),
    path('adminpanel',views.adminpanel,name="adminpanel"),
    path('home1',views.home1,name='home1'),
    path('profile',views.profile,name='profile'),
    path('edit_teacher/<int:pk>',views.edit_teacher,name="edit_teacher"),
    path('edit1_db/<int:pk>',views.edit1_db,name='edit1_db'),
    path('logoutpage',views.logoutpage,name='logoutpage'),

]
