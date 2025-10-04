from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializers import StudentSerializer 
import io 
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_student(request) : 
    if request.method == 'POST' : 
        json_data = request.body 
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream) 
        serializer = StudentSerializer(data=python_data) 
        if serializer.is_valid() : 
            serializer.save() 
            msg = {'msg' : 'Student Saved'}
            json_data = JSONRenderer().render(data=msg)
            return HttpResponse(json_data , content_type='application/json')
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data , content_type='application/json')
         
                