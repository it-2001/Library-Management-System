from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from .models import Kniha, Autor, Nakladatelstvi


def index(request):
    context = {
        'knihy': Kniha.objects.order_by('-strany')[:3],
        "autory": Autor.objects.order_by("jmeno"),
    }
    return render(request, 'index.html', context=context)


def seznam(request):
    context = {
        'knihy': Kniha.objects.order_by('strany'),
        "autory": Autor.objects.order_by("jmeno"),
    }
    return render(request, 'seznam.html', context=context)


class Detail_kniha(DetailView):
    model = Kniha
    template_name = "detail.html"
    context_object_name = "kniha"