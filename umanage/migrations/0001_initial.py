# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenAuthorization',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True, db_index=True)),
                ('created_dttm', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('last_modified_dttm', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('new_email_address', models.EmailField(max_length=254, blank=True, null=True)),
                ('expires', models.DateTimeField()),
                ('reason', models.CharField(max_length=50, blank=True, null=True)),
                ('created_user', models.ForeignKey(related_name='umanage_tokenauthorization_created_user+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_user', models.ForeignKey(related_name='umanage_tokenauthorization_last_modified_user+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountActivationAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('umanage.tokenauthorization',),
        ),
        migrations.CreateModel(
            name='ChangeEmailAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('umanage.tokenauthorization',),
        ),
        migrations.CreateModel(
            name='ForgotPasswordAuthorization',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('umanage.tokenauthorization',),
        ),
    ]
