from rest_framework import viewsets 
from api.models import Student 
from api.serializers import StudentSerializer 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, AllowAny, IsAdminUser

class StudentApi(viewsets.ModelViewSet) : 
   queryset = Student.objects.all() 
   serializer_class = StudentSerializer 

   # authentication_classes = [SessionAuthentication]
   # permission_classes = [IsAuthenticated]
   # permission_classes = [IsAuthenticatedOrReadOnly]
   # permission_classes = [DjangoModelPermissions]
   # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

   authentication_classes = [BasicAuthentication]
   # permission_classes = [AllowAny]
   # permission_classes = [IsAdminUser]   
   # permission_classes = [IsAuthenticated]   
   # permission_classes = [IsAuthenticatedOrReadOnly]   
   permission_classes = [IsAdminUser, DjangoModelPermissions]
   # permission_classes = [DjangoModelPermissions]





   