# Generated by Django 3.1.7 on 2021-02-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210228_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('icon-grid', 'quadrinhos'), ('icon-layers', 'design'), ('icon-bubbles', 'balões'), ('icon-briefcase', 'maleta')], max_length=14, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'servico',
                'verbose_name_plural': 'servicos',
            },
        ),
    ]
