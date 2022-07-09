from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes":lista_filmes}

def lista_filmes_popular(request):
    lista_filmes = Filme.objects.all().order_by('visualisacoes')[0:8]
    return {"lista_filmes_popular":lista_filmes}
