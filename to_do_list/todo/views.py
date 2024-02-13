from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"

class ItemListView(ListView):
    model = Item
    context_object_name = "items"


class ItemCreateView(CreateView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item


class ItemDeleteView(DeleteView):
    model = Item