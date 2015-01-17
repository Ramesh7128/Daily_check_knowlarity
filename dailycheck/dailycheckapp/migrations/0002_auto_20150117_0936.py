# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dailycheckapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='user',
            new_name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='users',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
