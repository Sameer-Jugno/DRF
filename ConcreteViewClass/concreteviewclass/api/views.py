from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Student 
from api.serializers import StudentSerializer

# single classes  
# class listStudentAPI(ListAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer 


# class createStudentAPI(CreateAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer 

   
# class updateStudentAPI(UpdateAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer 

   
# class deleteStudentAPI(DestroyAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer 
   
# class retrieveStudentAPI(RetrieveAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer 


# double Class  
# class listCreateStudentAPI(ListCreateAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer
   
# class retrieveDestroyCreateStudentAPI(RetrieveDestroyAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer

# class retrieveUpdateCreateStudentAPI(RetrieveUpdateAPIView) : 
#    queryset = Student.objects.all() 
#    serializer_class = StudentSerializer


class listCreateStudentAPI(ListCreateAPIView,) : 
   queryset = Student.objects.all() 
   serializer_class = StudentSerializer

class retrieveUpdateDestroyStudentAPI(RetrieveUpdateDestroyAPIView) : 
   queryset = Student.objects.all() 
   serializer_class = StudentSerializer