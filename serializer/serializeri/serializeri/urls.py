from django.contrib import admin
from django.urls import path
from api import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentInfo/<int:pk>', views.get_info , name='info'),
    path('studentInfos', views.get_infos, name='infos'),
]
