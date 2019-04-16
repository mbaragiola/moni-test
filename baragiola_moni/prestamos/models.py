from django.db import models
from django.urls import reverse

GENERO_MASCULINO = 'M'
GENERO_FEMENINO = 'F'
GENEROS = (
    (GENERO_MASCULINO, 'Masculino'),
    (GENERO_FEMENINO, 'Femenino')
)


class Pedido(models.Model):
    """
    Los clientes pueden pedir préstamos online sin registrarse
    en la plataforma.
    Los pedidos son autorizados o denegados utilizando una API de
    terceros.
    """
    dni = models.CharField(
        'DNI',
        max_length=10
    )
    nombre = models.CharField(
        'nombre',
        max_length=50
    )
    apellido = models.CharField(
        'apellido',
        max_length=50
    )
    genero = models.CharField(
        'genero',
        max_length=1,
        choices=GENEROS
    )
    email = models.EmailField(
        'email'
    )
    monto = models.DecimalField(
        'monto',
        max_digits=15,
        decimal_places=2
    )
    autorizado = models.BooleanField(
        'autorizado',
        blank=True,
        default=False
    )
    borrado = models.BooleanField(
        'borrado',
        blank=True,
        default=False
    )
    fecha = models.DateTimeField(
        'fecha',
        auto_now_add=True
    )
    fecha_ultima_modificacion = models.DateTimeField(
        'fecha última modificación',
        auto_now=True
    )

    def __str__(self):
        return "%(apellido)s, %(nombre)s (%(dni)s) - %(fecha)s" % {
            'apellido': self.apellido,
            'nombre': self.nombre,
            'dni': self.dni,
            'fecha': self.fecha.strftime('%d-%m-%Y %H:%M')
        }

    def get_absolute_url(self):
        return reverse('prestamos:pedido-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ['-fecha', 'apellido', 'nombre']
