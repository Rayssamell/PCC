# Generated by Django 4.1.5 on 2023-01-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atuacao_Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=150)),
                ('dia_hrs_atendimento', models.DateTimeField()),
                ('cpf_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universidade', models.CharField(max_length=150)),
                ('grau_academico', models.CharField(max_length=100)),
                ('especializacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalhos_academicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_trabalho', models.CharField(max_length=150)),
                ('autores', models.CharField(max_length=200)),
                ('revista', models.CharField(max_length=150)),
                ('ano', models.DateField()),
                ('cpf_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.IntegerField()),
                ('endereco', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=15)),
                ('descricao', models.TextField()),
            ],
        ),
    ]