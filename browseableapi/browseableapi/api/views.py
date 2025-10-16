from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from api.models import Student 
from api.serializers import StudentSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def student_api(request, pk = None) : 
    if request.method == 'GET' : 
        id = pk
        if id is not None : 
            stu = Student.objects.get(pk=id) 
            serializer = StudentSerializer(stu)
            return Response(serializer.data) 
        else : 
            stu = Student.objects.all() 
            serializers = StudentSerializer(stu, many=True) 
            return Response(serializers.data)
    
    if request.method == 'POST' : 
        serializer = StudentSerializer(data = request.data) 
        if serializer.is_valid() : 
            serializer.save() 
            return Response({'msg': 'Data Saved'})
        else : 
            return Response(serializer.errors)
        
    if request.method == 'PATCH' : 
        id = pk 
        stu = Student.objects.get(pk = id ) 
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid() : 
            serializer.save() 
            return Response({'msg' : 'Data Partial Updated','data' : serializer.data})
        else : 
            return Response(serializer.errors)
    
    if request.method == 'PUT' : 
        id = pk 
        stu = Student.objects.get(pk = id ) 
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid() : 
            serializer.save() 
            return Response({'msg' : 'Data Complete Updated', 'data' : serializer.data})
        else : 
            return Response(serializer.errors)
    
    if request.method == 'DELETE' : 
         
        stu = Student.objects.get(pk=pk) 
        stu.delete() 
        return Response({'msg' : f'Student Delete with id {pk}'})