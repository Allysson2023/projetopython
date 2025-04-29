from django.shortcuts import render, get_object_or_404, redirect
from contact.models import *
from django.db.models import Q

# Create your views here.
def index(request):

    return render (
        request,
        "global/base.html",
    )


def entregas(request):

    entregas = Entrega.objects.filter().order_by('-id')
    
    context = {
        'entregas' : entregas,
        'site_title' : 'Registros de Entregas -',
    }
    
    return render (
        request,
        'contact/index.html',
        context,
    )


def ocorrencia(request):

    ocorrencias = Ocorrencia.objects.filter().order_by('-id')

    context = {
        'ocorrencias': ocorrencias,
        'site_title' : 'Registros de Ocorrencias -',
    }

    return render (
        request,
        'contact/ocorencias.html',
        context,
    )

def entregas_id(request, entrega_id):

    # singles_entrega = Entrega.objects.filter(pk=entrega_id).first()
    singles_entrega = get_object_or_404(Entrega,pk=entrega_id )
    
    entregas = f'{singles_entrega.nome} '

    context = {
        'entrega' : singles_entrega,
        'site_title' : entregas,
    }
    
    return render (
        request,
        'contact/entrega_id.html',
        context,
    )

def ocorrencia_id(request, ocorrencia_id):

    singles_ocorrencias = get_object_or_404(Ocorrencia,pk=ocorrencia_id )
    
    context = {
        'ocorrencia' : singles_ocorrencias,
    }
    
    return render (
        request,
        'contact/ocorrencia_id.html',
        context,
    )

def search_entrega(request):
    search_entrega = request.GET.get('q', '').strip()

    if search_entrega == '':
        return redirect('contact:entregas')

    entregas = Entrega.objects\
        .filter()\
        .filter(
            Q(receberam__icontains=search_entrega)|
            Q( data__icontains=search_entrega) | 
            Q( apt__icontains=search_entrega) 
            )\
        .order_by('-id')
    
    context = {
        'entregas' : entregas,
        'site_title' : 'Search_entregas -',
        'search_entrega':search_entrega,
    }
    
    return render (
        request,
        'contact/index.html',
        context,
    )