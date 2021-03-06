# Generated by Django 3.1.7 on 2021-02-28 20:54

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('imagem', stdimage.models.StdImageField(upload_to='about', verbose_name='Imagem')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('experiencia', models.CharField(max_length=50, verbose_name='Experiência')),
                ('pais', models.CharField(default='Brasil', max_length=30, verbose_name='País')),
                ('local', models.CharField(max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=100, verbose_name='E-Mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Número')),
                ('freela', models.BooleanField(default=True, verbose_name='Disponível pra Freela?')),
            ],
            options={
                'verbose_name': 'sobre',
                'verbose_name_plural': 'sobres',
            },
        ),
    ]
