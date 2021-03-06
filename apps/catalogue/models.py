from django.db import models
from django.utils.translation import gettext_lazy as _

from oscar.apps.catalogue.abstract_models import AbstractProductClass

from .storages import DigitalProductStorage


class ProductClass(AbstractProductClass):
    is_downloadable = models.BooleanField(_('Is downloadable?'), default=False)


class ProductFile(models.Model):
    product = models.ForeignKey('catalogue.Product', related_name='files', on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)
    file = models.FileField(storage=DigitalProductStorage())
    checksum = models.CharField(max_length=150, null=True, blank=True)
    size = models.BigIntegerField()
    mimetype = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)

    def __str__(self):
        return self.filename


from oscar.apps.catalogue.models import *  # noqa isort:skip
