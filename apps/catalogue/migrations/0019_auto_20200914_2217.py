# Generated by Django 2.2.16 on 2020-09-14 16:47

import apps.catalogue.storages
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20191220_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='is_downloadable',
            field=models.BooleanField(default=False, verbose_name='Is downloadable?'),
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated')),
                ('file', models.FileField(storage=apps.catalogue.storages.DigitalProductStorage(), upload_to='')),
                ('checksum', models.CharField(blank=True, max_length=150, null=True)),
                ('size', models.BigIntegerField()),
                ('mimetype', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='catalogue.Product')),
            ],
        ),
    ]
