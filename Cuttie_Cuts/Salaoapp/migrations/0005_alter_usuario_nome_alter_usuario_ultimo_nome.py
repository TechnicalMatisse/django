# Generated by Django 4.1.1 on 2022-10-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salaoapp', '0004_alter_endereco_cep_alter_usuario_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ultimo_nome',
            field=models.CharField(max_length=25),
        ),
    ]
