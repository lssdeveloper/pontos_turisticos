# Generated by Django 3.1.7 on 2021-04-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
