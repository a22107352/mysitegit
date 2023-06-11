from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Projeto, Cadeira
from uuid import uuid4

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "login.html", {'message': "Invalid credentials."})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, 'index.html', {"message": "Logged out."})

@login_required
def projeto_cadeira_list(request):
    projetos = Projeto.objects.all()
    cadeiras = Cadeira.objects.all()
    return render(request, 'user.html', {'projetos': projetos, 'cadeiras': cadeiras})

@login_required
def projeto_cadeira_create(request):
    projetos = Projeto.objects.all()
    cadeiras = Cadeira.objects.all()
    if request.method == 'POST':
        if 'add_projeto' in request.POST:
            nome_projeto = request.POST['projeto_titulo']  # Updated key: projeto_titulo
            descricao_projeto = request.POST['projeto_descricao']  # Updated key: projeto_descricao
            Projeto.objects.create(titulo=nome_projeto, descricao=descricao_projeto, user=request.user)
            return redirect('index')
        if 'add_cadeira' in request.POST:
            nome_cadeira = request.POST['nome_cadeira']
            ranking_cadeira = request.POST['cadeira_ranking']
            ects_cadeira = request.POST['cadeira_ects']
            Cadeira.objects.create(nome=nome_cadeira, ranking=ranking_cadeira, ects=ects_cadeira, user=request.user)
            return redirect('index')
    return render(request, 'create_delete.html', {'projetos': projetos, 'cadeiras': cadeiras})

@login_required
def projeto_cadeira_delete(request, obj_type, obj_id):
    projetos = Projeto.objects.all()
    cadeiras = Cadeira.objects.all()
    if request.method == 'POST':
        if obj_type == 'projeto':
            try:
                projeto = Projeto.objects.get(id=obj_id)
                projeto.delete()
                return redirect('index')
            except Projeto.DoesNotExist:
                # Handle case when Projeto does not exist
                pass
        elif obj_type == 'cadeira':
            try:
                cadeira = Cadeira.objects.get(id=obj_id)
                cadeira.delete()
                return redirect('index')
            except Cadeira.DoesNotExist:
                # Handle case when Cadeira does not exist
                pass

        return redirect('index')

    return render(request, 'create_delete.html', {'projetos': projetos, 'cadeiras': cadeiras})
