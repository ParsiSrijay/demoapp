from django.urls import path
from . import views
urlpatterns = [
    path('addpol',views.addpolicy,name ='addpol'),
]
