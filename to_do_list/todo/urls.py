from django.urls import path
from .views import (ItemCreateView, ItemDeleteView, ItemDetailView, 
                    ItemListView, ItemUpdateView, CustomLoginView)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("", ItemListView.as_view(), name="item-list"),
    path("item-create/", ItemCreateView.as_view(), name="item-create"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("item/<int:pk>/delete", ItemDeleteView.as_view(), name="item-delete"),        
    path("item/<int:pk>/update", ItemUpdateView.as_view(), name="item-update"),
]