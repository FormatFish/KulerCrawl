from __future__ import unicode_literals

from django.db import models
from django_mysql.models import JSONField
# Create your models here.
class ColorPalette(models.Model):
	attrs = JSONField()