from django.urls import path
from . import views
from .views import generate_text

app_name = 'blogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index2'),
    path('gennsinn/', views.gennsinn, name='gennsinn'),
    path('houkai/', views.houkai, name='houkai'),
    path('apex/', views.apex, name='apex'),
    path('daigo5/', views.daigo5, name='daigo5'),
    path('varo/', views.varo, name='varo'),
    path('callback/', views.line_webhook, name='line_webhook'),
    path('line/', views.line_redirect, name='line_redirect'),
    path('your_template/', views.your_template, name='your_template'),
    path('generate/', generate_text, name='generate_text'),
]

