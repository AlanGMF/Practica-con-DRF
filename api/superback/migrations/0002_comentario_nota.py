# Generated by Django 4.0.4 on 2022-05-20 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='nota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='superback.nota'),
        ),
    ]
