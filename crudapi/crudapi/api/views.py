from django.shortcuts import render
from api.models import Student 
import io 
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Student_api(request) : 
    
    if request.method == 'GET':
        id = request.GET.get('id',None) 
        print(id)
        if id is not None : 
            stu = Student.objects.get(id=id) 
            serializer = StudentSerializer(stu) 
            json_data = JSONRenderer().render(serializer.data) 
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all() 
        serializer = StudentSerializer(stu,many=True) 
        json_data = JSONRenderer().render(serializer.data) 
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST' : 
        json_data = request.body 
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream) 

        serializer = StudentSerializer(data=python_data) 

        if serializer.is_valid() : 
            serializer.save() 
            response = {'res' : 'Data Saved'}
            json_data = JSONRenderer().render(response) 
            return HttpResponse(json_data, content_type='application/json')
        else : 
            json_data = JSONRenderer().render(serializer.errors) 
            return HttpResponse(json_data, content_type='application/json')
            
    if request.method == 'PUT' : 
        json_data = request.body 
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream) 

        id = python_data.get('id')
        student = Student.objects.get(id=id) 

        serializer = StudentSerializer(student, data=python_data)  
        # use partial = True for partial updation
        # serializer = StudentSerializer(student, data=python_data,partial=True)  

        if serializer.is_valid() : 
            serializer.save() 
            response = {'msg' : 'Data Updated'}
            json_data = JSONRenderer().render(response) 
            return HttpResponse(json_data, content_type='application/json')
        else : 
            json_data = JSONRenderer().render(serializer.errors) 
            return HttpResponse(json_data, content_type='application/json')
            
    if request.method == 'DELETE' : 
        
        json_data = request.body 
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream) 

        id = python_data.get('id')
        print(id)
        student = Student.objects.get(id=id)
        if student : 
            print('in if')

            student.delete() 
            response = {'msg' : 'Student Deleted'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type = 'application/json')
        else : 
            print('in else')
            response = {'msg' : 'Student not Deleted'}
            json_data = JSONRenderer().render()
            return HttpResponse(json_data, content_type = 'application/json')
