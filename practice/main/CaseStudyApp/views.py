from CaseStudyApp.Serializers import CaseStudySerializers
from django.shortcuts import render
from operator import inv
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from CaseStudyApp.models import CaseStudies
from django.core.files.storage import default_storage

from rest_framework import generics

@csrf_exempt
def casestudyApi(request,id=0):
    if request.method=="GET":
        if id==0:
            product= CaseStudies.objects.all();
            product_serializer= CaseStudySerializers(product,many=True)
            return JsonResponse(product_serializer.data, safe=False)
        else:
            product=CaseStudies.objects.get(id=id)
            product_serializer= CaseStudySerializers(product)
            return JsonResponse(product_serializer.data,safe=False)

    elif request.method=="POST":
        Product_data = JSONParser().parse(request)
        #print(request)
        product_serializer = CaseStudySerializers(data=Product_data)
        #print(product_serializer.is_valid())
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully!!", safe= False)
        return JsonResponse("Failed to add man!",safe= False)
    
    elif request.method=="PUT":
         Product_data= JSONParser().parse(request)
         product= CaseStudies.objects.get(id=Product_data['id'])
         product_serializer = CaseStudySerializers(product,data=Product_data)     
         if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("updated successfully", safe= False)
         return JsonResponse("failed to do man", safe=False)
@csrf_exempt
def SaveFile(request):
    file= request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)