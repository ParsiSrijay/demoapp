from django.urls import path
from . import views
urlpatterns = [
    path('feedback',views.feedbackrequest,name ='feedback'),
    path('aggr',views.aggr,name='agg'),
]
