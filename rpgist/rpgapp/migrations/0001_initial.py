# Generated by Django 3.2.9 on 2021-11-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('life', models.IntegerField()),
                ('str', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('int', models.IntegerField()),
                ('sab', models.IntegerField()),
                ('agi', models.IntegerField()),
                ('perm', models.CharField(choices=[('adm', 'Administrador'), ('com', 'Comum')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Habs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habname', models.CharField(max_length=250)),
                ('habdesc', models.TextField()),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpgapp.personagem')),
            ],
        ),
    ]
