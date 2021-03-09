# Generated by Django 3.1.7 on 2021-03-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=16)),
                ('cpf', models.CharField(max_length=14)),
                ('RG', models.CharField(max_length=9)),
                ('endereco', models.CharField(max_length=200)),
                ('complemento', models.TextField(blank=True, max_length=200, null=True)),
                ('cep', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
                ('esta_negativado', models.BooleanField()),
            ],
        ),
    ]