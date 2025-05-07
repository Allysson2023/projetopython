from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    #Inicial Index
    path('', views.index, name='index'),

    #Paginal Entregas
    path('entregas/', views.entregas, name='entregas'),
    path('search_entrega/', views.search_entrega, name='search_entrega'),
    
    #Pagina Ocorrencias
    path('ocorrencia/', views.ocorrencia, name='ocorrencia'),
    path('search_ocorrencia/', views.search_ocorrencia, name='search_ocorrencias'),
    
    #CRUD Entregas
    path('entregas/<int:entrega_id>/detail/', views.entregas_id, name='entregas_id'),
    path('entregas/create/', views.create_entregas, name='create_entregas'),
    path('entregas/<int:entrega_id>/update/', views.update_entregas, name='update_entregas'),
    path('entregas/<int:entrega_id>/delete/', views.delete_entrega, name='delete_entrega'),
    
    
    #CRUD Ocorrencias
    path('ocorrencia/<int:ocorrencia_id>/detail/', views.ocorrencia_id, name='ocorrencias_id'),
    path('ocorrencia/create/', views.create_ocorrencia, name='create_ocorrencia'),
    path('ocorrencia/<int:ocorrencia_id>/update/', views.update_ocorrencia, name='update_ocorrencia'),
    path('ocorrencia/<int:ocorrencia_id>/delete/', views.delete_ocorrencia, name='delete_ocorrencia'),

]