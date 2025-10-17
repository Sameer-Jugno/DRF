from django.contrib import admin
from django.urls import path
from api import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student_api/', views.listStudentAPI.as_view()),
    # path('student_api/', views.createStudentAPI.as_view()),
    # path('student_api/<int:pk>/', views.updateStudentAPI.as_view()),
    # path('student_api/<int:pk>/', views.deleteStudentAPI.as_view()),
    # path('student_api/<int:pk>/', views.retrieveStudentAPI.as_view()),
    # path('student_api/', views.listCreateStudentAPI.as_view()),
    # path('student_api/<int:pk>/', views.retrieveUpdateCreateStudentAPI.as_view()),


    path('student_api/', views.listCreateStudentAPI.as_view()),
    path('student_api/<int:pk>/', views.retrieveUpdateDestroyStudentAPI.as_view()),

]
