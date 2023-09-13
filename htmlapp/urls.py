from django.urls import path
from htmlapp.views import home,login_page , register,logout_view,about,furniture,addrecipe,recipelist,recipedelete,updaterecipe
urlpatterns = [
    path('home/',home , name='home'),
    path('login/',login_page , name='login_page'),
    path('register/',register , name='register'),
    path('logout/',logout_view , name='logout_view'),
    path('about/',about , name='about'),
    path('furniture/',furniture , name='furniture'),
    path('add/',addrecipe , name='addrecipe'),
    path('recipe/',recipelist , name='recipelist'),
    path('delete/<int:pk>',recipedelete, name='recipedelete'),
    path('update/<int:pk>',updaterecipe, name='updaterecipe'),

]