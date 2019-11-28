from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import signals
from django.dispatch import receiver
# Create your models here.


@receiver(signals.pre_save)
def update_ports(sender, instance, **kwargs):
    pass


class Asset(models.Model):
    hostname = models.CharField(
        blank=True,
        default=None,
        max_length=255,
        null=True,
        unique=True,
        verbose_name=_('hostname'),
    )
    max_ports = models.PositiveSmallIntegerField(
        verbose_name=_('max ports'),
        default=4,
        blank=True,
    )
    ports = models.ManyToManyField(
        'self',
        through='Port',
        symmetrical=False,
        blank=True,
        default=None,
        related_name='portss',
    )
    @property
    def port_count(self):
        """port count"""
        port_count = self.switch_ports.count() + self.server_ports.count()
        return port_count

    @property
    def port_to(self):
        """port to"""
        port_to = ['Link to: ' + str(self.__class__.objects.get(pk=item).hostname) for item in self.switch_ports.values_list('server_port_id', flat=True)]
        port_to = ';\n '.join(port_to)
        return port_to

    def __str__(self):
        return self.hostname


class Port(models.Model):
    server_port = models.ForeignKey(
        'Asset',
        blank=True,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name='server_ports',
    )
    server_number = models.PositiveSmallIntegerField(
        verbose_name=_('server number'),
        default=1,
        blank=False,
    )
    switch_port = models.ForeignKey(
        'Asset',
        blank=True,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name='switch_ports',
    )
    switch_number = models.PositiveSmallIntegerField(
        verbose_name=_('switch number'),
        default=1,
        blank=False,
    )

    def __str__(self):
        return self.switch_port

    class Meta:
        unique_together = ('server_port', 'switch_port')
