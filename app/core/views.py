from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomeTemplateView(TemplateView):
    template_name = 'core/base.html'


class HomeListView(ListView):
    template_name = 'core/lista.html'
    # context_object_name = 'object_list' # Para cambiar el nombre del object_list
    queryset = [2, 5, 7, 45, 3, 4, 67, 78, 5, 8]

