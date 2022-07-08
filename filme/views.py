from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
#Para cada view que for criar, tem que criar os 3 itens-> View - URL - Template

#Costruido com CBV - Class Base Views
class Homepage(TemplateView):
    template_name = 'homepage.html'

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme

class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        #contabilizar uma visualisação
        filme = self.get_object()
        filme.visualisacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) #redireciona o usuario para o url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja a categoria é igual a categoria do filme da página (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context



#Exemplo costruido com FBV - Functions Base Views

#def homepage(request):
#    return render(request, "homepage.html")

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request,'homefilmes.html', context)
