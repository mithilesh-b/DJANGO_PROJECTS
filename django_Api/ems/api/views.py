from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
# Create json response 

# def sample_data(request):
#     #name=['sanskar','mithilesh','ram','shyam']
#     # return JsonResponse(name,safe=False)   #expects dictionary type data...It allows the non dictionary objects to be serialized

#     student={'101':'Sanskar', '102':'Ram', '107':'Shyam'}
#     return JsonResponse(student)



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    