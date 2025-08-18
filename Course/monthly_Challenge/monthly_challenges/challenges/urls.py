# isme list banana hai 
from django.urls import path,re_path;
from . import views; 

urlpatterns=[
     # path("january",views.january),
     # path("february",views.february)
     # <int:bla bla> they are knows as path converters
     path("",views.index , name="index"),
     path("<int:month>",views.monthly_challenge_by_number),
     path("<str:month>",views.monthly_challenges,name="month-challenge"),
     re_path(r"^username/(?P<username>[a-zA-Z0-9_]+)/$",views.regex,name="regex"),
     
     ]