from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from baragiola_moni.prestamos import models


class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = models.Pedido
    context_object_name = 'pedido'
    template_name = 'prestamos/pedido_detail.html'


class PedidoCreateView(CreateView):
    model = models.Pedido
    fields = ['dni', 'nombre', 'apellido', 'email', 'genero', 'monto']
    template_name = 'prestamos/pedido_add.html'


class PedidosList(LoginRequiredMixin, ListView):
    template_name = 'prestamos/pedidos_list.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        return models.Pedido.objects.filter(borrado=False)


class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Pedido
    fields = [
        'dni',
        'nombre',
        'apellido',
        'email',
        'genero',
        'monto',
        'autorizado',
        'borrado'
    ]
    template_name = 'prestamos/pedido_edit.html'
