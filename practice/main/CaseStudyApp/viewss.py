import re
from django.http import JsonResponse
from casestudy.cognitivesearch.oDatfilter import oDataFilter
from casestudy.cognitivesearch.aiFilter import aiFilter
from django.shortcuts import render
from operator import inv
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from CaseStudyApp.models import CaseStudies
from django.core.files.storage import default_storage
from CaseStudyApp.Serializers import CaseStudySerializers
from rest_framework import generics
import json, os
from casestudy.connectdb import get_all,get_file,get_row,update_data,add_data,getaiFiltereddata
from main.casestudy.blobClient import upload
#import ssl
#os.environ['REQUESTS_CA_BUNDLE']= r'C:\Users\10710591\AppData\Local\Programs\Python\Python311\Lib\site-packages\certifi\cacert.pem'
@csrf_exempt
def filter_endpoint(request):
    if request.method=="POST":
        body_content = request.body.decode('utf-8')
        body_content=json.loads(body_content)
        vertical = body_content.get('Vertical')
        account = body_content.get('Account')
        service_offering_mapping = body_content.get('ServiceOfferingMapping')
        metadata = body_content.get('MetaData')
        rating = body_content.get('Rating')
        customer_reference=body_content.get('CustomerReferenceable')
        tag= body_content.get('Key')
        if vertical!=None:
            vertical= str(vertical)
        else:
            vertical=None
        if account!=None:
            account= str(account)
        else: 
            account=None
        if service_offering_mapping!=None:
            service_offering_mapping= str(service_offering_mapping)
        else:
            service_offering_mapping=None
        if metadata!=None:
            metadata= str(metadata)
        else:
            metadata=None
        if rating!=None:
            rating= str(rating)
        else:
            rating=None
        if customer_reference!=None:
            customer_reference=str(customer_reference)
        else:
            customer_reference=None
        if tag!=None:
            tag=str(tag)
        else:
            tag=None
        if tag==None:
            filtered_data = oDataFilter(account,vertical,service_offering_mapping,metadata,rating)
            return JsonResponse(json.loads(filtered_data),safe=False)
        elif(account==None and vertical==None and service_offering_mapping==None and metadata==None and rating==None and customer_reference==None and tag!=None ):
            filename=aiFilter(tag)
            ans=[]
            for file in filename:
                val= getaiFiltereddata(filename[file])
                if (val!=None):
                    ans.append(val)
            return JsonResponse(ans,safe=False)
        else:
            filename=aiFilter(tag)
            val=oDataFilter(account,vertical,service_offering_mapping,metadata,rating)
            ans=[]
            for value in val:
                for file in filename:
                    if (filename[file]==val[value].FileName):
                        ans.append(val[value])
            return JsonResponse(ans,safe=False)
        
    #service_offering_mapping = body_content.get('ServiceOfferingMapping', None)
    #metadata = body_content.get('MetaData', None)
    #rating = body_content.get('Rating', None)
    # Call the oDataFilter function passing the filter parameters
        #filtered_data = oDataFilter(account,vertical,service_offering_mapping,metadata,rating)
    # Return the filtered data as a JSON response
        #ssl._create_default_https_context = ssl._create_unverified_context
        #return JsonResponse(json.loads(filtered_data),safe=False)
        #return JsonResponse("error :invalid request method",status=405,safe=False)
@csrf_exempt
def get_case_id(request,id):
    if request.method=="GET":
        try:
            product=CaseStudies.objects.get(id=id)
            product_serializer= CaseStudySerializers(product)
            return JsonResponse(product_serializer.data,safe=False)
        except:
            return JsonResponse(("Sorry!  Your case id={} is not found!").format(id),safe=False)
@csrf_exempt
def get_all_cases(request):
    if request.method=="GET":
        product= CaseStudies.objects.all()
        product_serializer= CaseStudySerializers(product,many=True)
        return JsonResponse(product_serializer.data, safe=False)
@csrf_exempt
def add_image_api(request):
    if request.method=="POST":
        body_content = request.body.decode('utf-8')
        body_content=json.loads(body_content)
        name=body_content.get('CaseStudyName')
        vertical = body_content.get('Vertical')
        account = body_content.get('Account')
        solution= body_content.get('SolutionName')
        spoc= body_content.get('spoc')
        status=body_content.get('Status')
        filename=body_content.get('FileName')
        year= body_content.get('Year')
        casestudy_poc=body_content.get('CaseStudyPOC')
        service_offering_mapping = body_content.get('ServiceOfferingMapping')
        metadata = body_content.get('MetaData')
        rating = body_content.get('Rating')
        customer_reference=body_content.get('CustomerReferenceable')
        dependency=body_content.get('Dependency')
        add_data(name,account,vertical,spoc,solution,service_offering_mapping,status,metadata,filename,rating,year,casestudy_poc,customer_reference,dependency)
        file=request.FILES['filename']
        if(file!=None):
            upload(file,file.name)
        else:
            return JsonResponse("No file")
        return JsonResponse("added successfully!")
def update_image(request):
    if request.method=="PUT":
        body_content = request.body.decode('utf-8')
        body_content=json.loads(body_content)
        id=body_content.get('id')
        id=int(id)
        name=body_content.get('CaseStudyName')
        vertical = body_content.get('Vertical')
        account = body_content.get('Account')
        solution= body_content.get('SolutionName')
        spoc= body_content.get('spoc')
        status=body_content.get('Status')
        filename=body_content.get('FileName')
        year= body_content.get('Year')
        casestudy_poc=body_content.get('CaseStudyPOC')
        service_offering_mapping = body_content.get('ServiceOfferingMapping')
        metadata = body_content.get('MetaData')
        rating = body_content.get('Rating')
        customer_reference=body_content.get('CustomerReferenceable')
        dependency=body_content.get('Dependency')
        update_data(id, name, account, vertical, spoc, solution, service_offering_mapping, status, metadata, filename, rating, year, casestudy_poc, customer_reference, dependency)
        file=request.FILES['filename']
        if(file!=None):
            upload(file,file.name)
        else:
            return JsonResponse("No file")
        return JsonResponse("updated successfully!")
    