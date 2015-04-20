# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountActivationAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('django_core.tokenauthorization',),
        ),
        migrations.CreateModel(
            name='ChangeEmailAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('django_core.tokenauthorization',),
        ),
        migrations.CreateModel(
            name='ForgotPasswordAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('django_core.tokenauthorization',),
        ),
    ]
