from rest_framework import viewsets 
from api.models import Student 
from api.serializers import StudentSerializer 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class StudentApi(viewsets.ModelViewSet) : 
   queryset = Student.objects.all() 
   serializer_class = StudentSerializer 

   authentication_classes = [BasicAuthentication] 
   permission_classes = [AllowAny] 
