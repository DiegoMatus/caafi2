# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0012_language_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='slug',
        ),
    ]