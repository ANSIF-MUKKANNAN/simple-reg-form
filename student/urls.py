from django.urls import path
from .import views
urlpatterns = [
    path('',views.insert,name='register'),
    path('views/',views.view,name='views'),
    path('detailview/<str:pk>',views.detailview,name='detailview'),
    path('update/<str:pk>/',views.update,name="update"),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('alogin/',views.alogin,name='alogin'),
]
    