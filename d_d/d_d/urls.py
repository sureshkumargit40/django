"""d_d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basic_d import views

app_name ='basic_d'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('keyperformance',views.Keyperformance,name='keyperformance'),  # indicator 2 & KPI Link
    path('financial',views.Financial,name='financial'),
    path('analysis',views.Analysis,name='analysis'),
    path('user/',views.user,name='user'),
    path('portfolio/',views.Portfolio,name='portfolio'),
    path('programm/',views.Program,name='program'),
    path('department/',views.department,name='department'),
    path('district/',views.district,name='district'),
    path('report/',views.Report_Year,name='report'),
    path('state_report/',views.State_Report,name='state_report'),
    path('help/',views.Help_Cont,name='help'),
    path('indicator_1/',views.Family_Health,name='indicator_1'),   #indicator 1
    path('indicator_9/',views.Pichart,name='indicator_9'),   #indicator 3
    path('calendar/',views.Calendar,name='calendar'),
    path('add/',views.Calendar_Add,name='add'),
    path('entry/<int:pk>',views.Calendar_Details,name='details'),
    path('chatapp/',views.Chat_Report,name='chat'),

]
