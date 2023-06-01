from django.urls import re_path,path
import importlib

#from CaseStudyApp.viewss import get_all,get_all_cases,get_case_id
from .viewss import get_case_id,get_all_cases
from CaseStudyApp import viewss
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('allCases/',get_all_cases,name="getallcasesapi"),
    path('new/',viewss.newapi,name="api"),
    #re_path(r'^case/([0-9]+)$',views.casestudyApi),
    path('case/<int:id>/',get_case_id, name='getcasewithid'),
    path('filter/', viewss.filter_endpoint, name='filter'),
    #re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


