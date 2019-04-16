from django.apps import AppConfig
from django.db.models.signals import pre_save


class PrestamosAppConfig(AppConfig):

    name = "baragiola_moni.prestamos"
    verbose_name = "Prestamos"

    def ready(self):
        from baragiola_moni.prestamos import models, signals

        pre_save.connect(
            receiver=signals.autorizar,
            sender=models.Pedido,
            dispatch_uid='Prestamos_Pedido_ChequearAutorizacion',
            weak=False
        )
