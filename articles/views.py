from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Articles
# Create your views here.


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'articles_new.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('article_list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(). form_valid(form)

class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'articles_list.html'



class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ('title', 'body',)
    template_name = 'articles_edit.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.author == self.request.user 

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'articles_detail.html'