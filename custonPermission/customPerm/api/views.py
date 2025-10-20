from rest_framework import viewsets 
from api.models import Student 
from api.serializers import StudentSerializer 
from rest_framework.authentication import SessionAuthentication
from api.custompermissions import MyPermission 

class StudentApi(viewsets.ModelViewSet) : 
   queryset = Student.objects.all() 
   serializer_class = StudentSerializer 

   authentication_classes = [SessionAuthentication]
   permission_classes = [MyPermission]




   