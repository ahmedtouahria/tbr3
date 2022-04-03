from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('create',views.create,name='create'),
    path('searchPerson',csrf_exempt(views.search_person),name='search_person'),
   # path('userCreate',views.user_create,name='user_create'),
    
    
    
]

