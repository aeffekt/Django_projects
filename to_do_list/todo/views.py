from .models import Item
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('item-list')


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = "item"


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        context['items'] = context['items'].filter(done_status=False)
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item    
    fields = {'title', 'description', 'done_status'}
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('item-list')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = "item"
    success_url = reverse_lazy('item-list')