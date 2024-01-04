from .import views
from django.urls import path
from django.urls import path
app_name='schoolapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('com',views.com,name='com'),
    path('comp',views.comp,name='comp'),
    path('maths',views.maths,name='maths'),
    path('stati',views.stati,name='stati'),
    path('mng',views.mng,name='mng'),
    path('register/',views.Register,name='Register'),
    path('login/',views.login,name='login'),
    path('new/',views.New,name='New'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load/', views.load, name='ajax_load'), # AJAX
    path('logout',views.logout,name='logout'),

    

]

    