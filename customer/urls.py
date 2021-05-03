from django.urls import path, include
from . import views

app_name = 'customer'
urlpatterns = [
   path('',views.home,name='home'),
   path('information/',views.information,name='information'),
   path('transfer_money/',views.transfer_money,name='transfer_money'),
   path('contact/',views.contact,name='contact'),
]