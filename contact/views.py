from django.shortcuts import render, get_object_or_404, redirect
from contact.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.urls import reverse
from contact.forms import *

# Create your views here.
def index(request):

    return render (
        request,
        "global/base.html",
    )

def entregas(request):

    entregas = Entrega.objects.filter().order_by('-id')

    paginator = Paginator(entregas , 10)
    page_number = request.GET.get("page")
    entrega_page_obj = paginator.get_page(page_number)
    
    context = {
        'entrega_page_obj' : entrega_page_obj,
        'site_title' : 'Registros de Entregas -',
    }
    
    return render (
        request,
        'contact/index.html',
        context,
    )

def ocorrencia(request):

    ocorrencias = Ocorrencia.objects.filter().order_by('-id')

    paginator = Paginator(ocorrencias , 10)
    page_number = request.GET.get("page")
    ocorrencia_page_obj = paginator.get_page(page_number)

    context = {
        'ocorrencia_page_obj': ocorrencia_page_obj,
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
    
    paginator = Paginator(entregas , 10)
    page_number = request.GET.get("page")
    entrega_page_obj = paginator.get_page(page_number)
    
    context = {
        'entrega_page_obj' : entrega_page_obj,
        'site_title' : 'Search_entregas -',
        'search_entrega':search_entrega,
    }
    
    return render (
        request,
        'contact/index.html',
        context,
    )

def search_ocorrencia(request):
    search_ocorrencias = request.GET.get('q', '').strip()

    if search_ocorrencias == '':
        return redirect('contact:search_ocorrencias')

    ocorrencias = Ocorrencia.objects\
        .filter()\
        .filter(
            Q(data__icontains=search_ocorrencias)|
            Q(nomeResp__icontains=search_ocorrencias)
            )\
        .order_by('-id')
    
    paginator = Paginator(ocorrencias , 10)
    page_number = request.GET.get("page")
    ocorrencia_page_obj = paginator.get_page(page_number)

    
    context = {
        'ocorrencia_page_obj' : ocorrencia_page_obj,
        'site_title' : 'Search_ocorrencias -',
        'search_ocorrencias':search_ocorrencias,
    }
    
    return render (
        request,
        'contact/ocorencias.html',
        context,
    )

 
def create_entregas(request):
    form_action = reverse('contact:create_entregas')

    if request.method == 'POST':
        form_entrega = EntregasForm(request.POST, request.FILES)
        context = {
            'form': form_entrega,
            'form_action' : form_action,
        }
        if form_entrega.is_valid():
            form_entrega.save()
            return redirect('contact:entregas')

        return render (
            request,
            'contact/create_entrega.html',
            context,
        )
    
    context = {
        'form':EntregasForm(),
        'form_action' : form_action,
    }
    return render (
        request,
        'contact/create_entrega.html',
        context,
    )

def update_entregas(request, entrega_id):
    entregas = get_object_or_404(Entrega, pk=entrega_id,)

    form_action = reverse('contact:update_entregas', args=(entrega_id,))

    if request.method == 'POST':
        form_entrega = EntregasForm(request.POST, request.FILES, instance=entregas)
        context = {
            'form': form_entrega,
            'form_action' : form_action,
        }
        if form_entrega.is_valid():
            entregas = form_entrega.save()
            return redirect('contact:entregas_id', entrega_id=entregas.pk)

        return render (
            request,
            'contact/create_entrega.html',
            context,
        )
    
    context = {
        'form':EntregasForm(instance=entregas),
        'form_action' : form_action,
    }
    return render (
        request,
        'contact/create_entrega.html',
        context,
    )

def create_ocorrencia(request):
    form_action = reverse('contact:create_ocorrencia')
    if request.method == 'POST':
        form_ocorrencia = OcorrenciaForm(request.POST)
        context = {
            'forms': form_ocorrencia,
            'form_action' : form_action,
        }

        if form_ocorrencia.is_valid():
            form_ocorrencia.save()
            return redirect('contact:ocorrencia')

        return render (
            request,
            'contact/create_ocorrencia.html',
            context,
        )

    context = {
        'forms':OcorrenciaForm(),
        'form_action' : form_action,
    }
    return render (
        request,
        'contact/create_ocorrencia.html',
        context,
    )

def update_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    form_action = reverse('contact:update_ocorrencia', args=(ocorrencia_id,))

    if request.method == 'POST':
        form_ocorrencia = OcorrenciaForm(request.POST, instance=ocorrencia)
        context = {
            'forms': form_ocorrencia,
            'form_action' : form_action,
        }

        if form_ocorrencia.is_valid():
            ocorrencia= form_ocorrencia.save()
            return redirect('contact:ocorrencias_id', ocorrencia_id=ocorrencia.pk)

        return render (
            request,
            'contact/create_ocorrencia.html',
            context,
        )

    context = {
        'forms':OcorrenciaForm(instance=ocorrencia),
        'form_action' : form_action,
    }
    return render (
        request,
        'contact/create_ocorrencia.html',
        context,
    )


def delete_entrega(request, entrega_id):
    entregas = get_object_or_404(Entrega, pk=entrega_id,)
    entregas.delete()
    return redirect('contact:entregas')

def delete_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    ocorrencia.delete()
    return redirect('contact:ocorrencia')