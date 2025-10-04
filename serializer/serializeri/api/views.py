from django.shortcuts import render, HttpResponse
from api.models import Student 
from api.serializers import StudentSerializer
import json
from rest_framework.renderers import JSONRenderer 
from django.http import JsonResponse

# Create your views here.
def get_info(request,pk) : 
    students = Student.objects.get(pk=pk)
    serializer = StudentSerializer(students) 
    # json_data = JSONRenderer().render(serializer.data) 
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def get_infos(request) : 
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) 
    # json_data = JSONRenderer().render(serializer.data) 
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False) 
    #Safe = False : It can display non-dict data as well