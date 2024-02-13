from django.urls import path
from .views import ItemCreateView, ItemDeleteView, ItemDetailView, ItemListView, ItemUpdateView

urlpatterns = [
    path("", ItemListView.as_view(), name="list-item"),
    path("todo/item/create/", ItemCreateView.as_view(), name="item-create"),
    path("todo/item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("todo/item/<int:pk>/delete", ItemDeleteView.as_view(), name="item-delete"),        
    path("todo/item/<int:pk>/update", ItemUpdateView.as_view(), name="item-update"),
]