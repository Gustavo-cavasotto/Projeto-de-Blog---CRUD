from audioop import reverse
from http.client import HTTPResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from . models import Post
from .forms import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #coloque isso, nos campos onde vc n quer que o usuário mexa, se não estiver logado

# Create your views here.
@login_required
def hello(request):
    return HttpResponse('Ola mundo')

class BlogListView(ListView):   #list view é um método para mostrar o models em lista
    model = Post
    template_name = 'blog/home.html'  #em qual arquivo vc quer aplicar a classe
    
class BlogDetailView(DetailView): #clicar no post e abrir uma página exibindo só ele
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'
    
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView): #criar post
    model = Post
    template_name = 'blog/post_new.html'
    form_class = Postform
    #exibir todos os campos da tabela, na tela de cadastro no formulário
    success_message = "%(field)s - Criado com sucesso"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
   
class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Post
    form_class = Postform
    template_name = 'blog/post_edit.html'
    #fields = ('titulo', 'conteudo', 'slug')
    success_message = "%(field)s - Alterado com sucesso"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
    
class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Excluido com sucesso"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)
    