from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('entregas/', views.entregas, name='entregas'),
    path('entregas/<int:entrega_id>/', views.entregas_id, name='entregas_id'), #entrega_id
    path('ocorrencia/', views.ocorrencia, name='ocorrencia'),
    path('ocorrencia/<int:ocorrencia_id>/', views.ocorrencia_id, name='ocorrencias_id'),

    path('search_entrega/', views.search_entrega, name='search_entrega'),

]