from django.urls import path

from baragiola_moni.prestamos import views

app_name = 'prestamos'
urlpatterns = [
    path(
        'pedidos/',
        view=views.PedidosList.as_view(),
        name='pedido-list'
    ),
    path(
        'pedidos/add/',
        view=views.PedidoCreateView.as_view(),
        name='pedido-create'
    ),
    path(
        'pedidos/<int:pk>/',
        view=views.PedidoDetailView.as_view(),
        name='pedido-detail'
    ),
    path(
        'pedidos/<int:pk>/edit/',
        view=views.PedidoUpdateView.as_view(),
        name='pedido-update'
    )
]
